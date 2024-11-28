import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import tempfile
import os

# Установим по умолчанию размер фигуры для Matplotlib по умолчанию.
matplotlib.rcParams['figure.figsize'] = [9, 6]

import tensorflow as tf
import tensorflow_datasets as tfds

def xavier_init(shape):
    # Вычисляем значения инициализации xavier для весовой матрицы
    in_dim, out_dim = shape
    # Задаем диапазон инициализации весов по схеме Ксавье
    xavier_lim = tf.sqrt(6.) / tf.sqrt(tf.cast(in_dim + out_dim, tf.float32))
    # Возвращаем тензор с равномерно распределенными случайными величинами в указанном интервале.
    weight_vals = tf.random.uniform(shape=(in_dim, out_dim), minval=-xavier_lim, maxval=xavier_lim)
    return weight_vals

class DenseLayer(tf.Module):
    def __init__(self, out_dim, weight_init=xavier_init, activation=tf.identity):
        """Инициализация размеров и функции активации"""
        self.out_dim = out_dim  # Определяем размерность выходов
        self.weight_init = weight_init  # Инициализируем веса
        self.activation = activation  # Задаем функцию активации
        self.built = False

    @tf.function
    def __call__(self, x):
        if not self.built:  # Если запущен первый раз проводим инициализацию
            # Вывод входного измерения на основе первого вызова
            self.in_dim = x.shape[1]
            # Инициализация весов и смещений
            self.w = tf.Variable(self.weight_init(shape=(self.in_dim, self.out_dim)))  # Объявление тензорных переменных
            self.b = tf.Variable(tf.zeros(shape=(self.out_dim,)))  # Объявление тензорных переменных
            self.built = True  # Инициализация пройдена
        # Вычисление прямого прохода
        y = tf.add(tf.matmul(x, self.w), self.b)  # уравнение персептрона
        return self.activation(y)  # Применение функции активации к уравнению персептрона

class MLP(tf.Module):
    def __init__(self, layers):
        self.layers = layers

    @tf.function  # Декоратор, который переносит вычисления на уровень графа TensorFlow
    def __call__(self, x, preds=False):
        # Последовательное выполнение слоев модели
        for layer in self.layers:
            x = layer(x)
        return x

class Adam:
    def __init__(self, learning_rate=1e-3, beta_1=0.9, beta_2=0.999, ep=1e-7):
        # Инициализируем параметры оптимизатора и резервируем переменные
        self.beta_1 = beta_1  # гиперпараметр
        self.beta_2 = beta_2  # гиперпараметр
        self.learning_rate = learning_rate  # шаг обучения
        self.ep = ep  # Эпсилон - предотвращает деление на ноль, слабо влияет на обучение
        self.t = 1.
        self.v_dvar, self.s_dvar = [], []
        self.built = False

    def apply_gradients(self, grads, vars):
        # Инициализируем переменные при первом вызове
        if not self.built:
            for var in vars:
                v = tf.Variable(tf.zeros(shape=var.shape))
                s = tf.Variable(tf.zeros(shape=var.shape))
                self.v_dvar.append(v)
                self.s_dvar.append(s)
            self.built = True
        # Обновите переменные модели с учетом их градиентов
        for i, (d_var, var) in enumerate(zip(grads, vars)):
            self.v_dvar[i].assign(self.beta_1 * self.v_dvar[i] + (1 - self.beta_1) * d_var)
            self.s_dvar[i].assign(self.beta_2 * self.s_dvar[i] + (1 - self.beta_2) * tf.square(d_var))
            v_dvar_bc = self.v_dvar[i] / (1 - (self.beta_1 ** self.t))
            s_dvar_bc = self.s_dvar[i] / (1 - (self.beta_2 ** self.t))
            var.assign_sub(self.learning_rate * (v_dvar_bc / (tf.sqrt(s_dvar_bc) + self.ep)))
        self.t += 1.
        return

def preprocess(x, y):
    """Функция изменения формы и масштабирования данных"""
    # reshap - изменяет форму данных
    x = tf.reshape(x, shape=(-1, 784))  # -1 - значит сохранить форму для заданного индекса матрицы, равносильно указать 1500
    # Масштабируем данные
    x = x / 255
    return x, y

def cross_entropy_loss(y_pred, y):
    # Вычисление перекрестной энтропии с помощью разреженной операции
    sparse_ce = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=y_pred)
    return tf.reduce_mean(sparse_ce)  # аналог np.mean для тензоров

def accuracy(y_pred, y):
    # Вычисляем точность после извлечения предсказаний класса
    class_preds = tf.argmax(tf.nn.softmax(y_pred), axis=1)  # возвращает индекс максимального элемента
    is_equal = tf.equal(y, class_preds)  # сравнение тензорных значений
    return tf.reduce_mean(tf.cast(is_equal, tf.float32))  # аналог np.mean для тензоров

train_data, val_data, test_data = tfds.load("fashion_mnist",
                                            split=['train[10000:]', 'train[0:10000]', 'test'],
                                            batch_size=128, as_supervised=True)

x_viz, y_viz = tfds.load("fashion_mnist", split=['train[:1500]'], batch_size=-1, as_supervised=True)[0]  # Взять все одним батчем и выбрать его для визуализации
print('Размерность исходных данных:', x_viz.shape)
x_viz = tf.squeeze(x_viz, axis=3)  # метод сжатия размерности, исключаем данные по оси с индексом 3
print('Размерность данных после сжатия:', x_viz.shape)

train_data, val_data = train_data.map(preprocess), val_data.map(preprocess)  # map выполняет функцию preprocess для каждого элемента данных, к которым применяется

hidden_layer_1_size = 700
hidden_layer_2_size = 500
output_size = 10

# Создание модели нейронной сети
mlp_model = MLP([
    DenseLayer(out_dim=hidden_layer_1_size, activation=tf.nn.relu),
    DenseLayer(out_dim=hidden_layer_2_size, activation=tf.nn.relu),
    DenseLayer(out_dim=output_size)])

x = tf.Variable(-2.0)

with tf.GradientTape() as tape:
    y = x ** 2

df = tape.gradient(y, x)
print(df)

def train_step(x_batch, y_batch, loss, acc, model, optimizer):
    # Обновляем состояние модели с учетом пакета данных
    with tf.GradientTape() as tape:
        y_pred = model(x_batch)  # Предсказываем значение с текущими весами
        batch_loss = loss(y_pred, y_batch)  # Оцениваем ошибку на текущих весах
        batch_acc = acc(y_pred, y_batch)  # Оцениваем точность на текущих весах
        grads = tape.gradient(batch_loss, model.variables)  # Вычисляем градиенты
        optimizer.apply_gradients(grads, model.variables)  # Обновляем переменные с учетом полученных градиентов
    return batch_loss, batch_acc  # Возвращаем ошибку и точность на основе заданного пакета

def val_step(x_batch, y_batch, loss, acc, model):
    # Оцениваем модель на основе заданного пакета валидационных данных без обучения на текущих весах
    y_pred = model(x_batch)
    batch_loss = loss(y_pred, y_batch)
    batch_acc = acc(y_pred, y_batch)
    return batch_loss, batch_acc

def train_model(mlp, train_data, val_data, loss, acc, optimizer, epochs):
    # Инициализация структур данных
    train_losses, train_accs = [], []
    val_losses, val_accs = [], []

    # Отформатируем тренировочный цикл и начнем обучение
    for epoch in range(epochs):
        batch_losses_train, batch_accs_train = [], []
        batch_losses_val, batch_accs_val = [], []

        # Выполняем итерацию по обучающим данным
        for x_batch, y_batch in train_data:
            # Вычисляем градиенты и обновляем параметры модели
            batch_loss, batch_acc = train_step(x_batch, y_batch, loss, acc, mlp, optimizer)
            # Следим за результатами обучения на пакетном уровне
            batch_losses_train.append(batch_loss)
            batch_accs_train.append(batch_acc)

        # Повторяем процедуру проверки данных
        for x_batch, y_batch in val_data:
            batch_loss, batch_acc = val_step(x_batch, y_batch, loss, acc, mlp)
            batch_losses_val.append(batch_loss)
            batch_accs_val.append(batch_acc)

        # Следим за производительностью модели на уровне эпохи
        train_loss, train_acc = tf.reduce_mean(batch_losses_train), tf.reduce_mean(batch_accs_train)
        val_loss, val_acc = tf.reduce_mean(batch_losses_val), tf.reduce_mean(batch_accs_val)
        train_losses.append(train_loss)
        train_accs.append(train_acc)
        val_losses.append(val_loss)
        val_accs.append(val_acc)
        print(f"Эпоха: {epoch}")
        print(f"Обучающая ошибка: {train_loss:.3f}, Обучающая точность: {train_acc:.3f}")
        print(f"Валидационная ошибка: {val_loss:.3f}, Валидационная точность: {val_acc:.3f}")
    return train_losses, train_accs, val_losses, val_accs

train_losses, train_accs, val_losses, val_accs = train_model(mlp_model, train_data, val_data,
                                                             loss=cross_entropy_loss, acc=accuracy,
                                                             optimizer=Adam(), epochs=10)

def plot_metrics(train_metric, val_metric, metric_type):
    # Визуализация метрик в зависимости от эпох обучения
    plt.figure()
    plt.plot(range(len(train_metric)), train_metric, label=f"{metric_type} на обучающей выборке")
    plt.plot(range(len(val_metric)), val_metric, label=f"{metric_type} на валидационной выборке")
    plt.xlabel("Эпохи")
    plt.ylabel(metric_type)
    plt.legend()
    plt.title(f"{metric_type} от эпохи")
    plt.show()

plot_metrics(train_losses, val_losses, "Ошибка перекрестной энтропии")
plot_metrics(train_accs, val_accs, "точность")

class ExportModule(tf.Module):
    def __init__(self, model, preprocess, class_pred):
        # Инициализация функций предобработки и постобработки
        self.model = model
        self.preprocess = preprocess
        self.class_pred = class_pred

    @tf.function(input_signature=[tf.TensorSpec(shape=[None, None, None, None], dtype=tf.uint8)])
    def __call__(self, x):
        # Запускаем модуль экспорта для получения новых точек данных
        x = self.preprocess(x)
        y = self.model(x)
        y = self.class_pred(y)
        return y

def preprocess_test(x):
    # Модуль экспорта принимает необработанные и немаркированные данные
    x = tf.reshape(x, shape=[-1, 784])
    x = x / 255
    return x

def class_pred_test(y):
    # Сгенерируем прогнозы классов на основе выходных данных MLP
    return tf.argmax(tf.nn.softmax(y), axis=1)

mlp_model_export = ExportModule(model=mlp_model,
                                preprocess=preprocess_test,
                                class_pred=class_pred_test)

models = tempfile.mkdtemp()
save_path = os.path.join(models, 'mlp_model_export')
tf.saved_model.save(mlp_model_export, save_path)

mlp_loaded = tf.saved_model.load(save_path)

def accuracy_score(y_pred, y):
    # Общая функция точности
    is_equal = tf.equal(y_pred, y)
    return tf.reduce_mean(tf.cast(is_equal, tf.float32))

x_test, y_test = tfds.load("fashion_mnist", split=['test'], batch_size=-1, as_supervised=True)[0]
test_classes = mlp_loaded(x_test)
test_acc = accuracy_score(test_classes, y_test)
print(f"Точность на тестовой выборке: {test_acc:.3f}")

print("Точность с разбивкой по цифрам :")
print("---------------------------")
label_accs = {}
for label in range(10):
    label_ind = (y_test == label)
    # extract predictions for specific true label
    pred_label = test_classes[label_ind]
    labels = y_test[label_ind]
    # compute class-wise accuracy
    label_accs[accuracy_score(pred_label, labels).numpy()] = label
for key in sorted(label_accs):
    print(f"Цифра {label_accs[key]}: {key:.3f}")

import sklearn.metrics as sk_metrics

def show_confusion_matrix(test_labels, test_classes):
    # Вычисление матрицы ошибок и ее нормализация
    plt.figure(figsize=(10, 10))
    confusion = sk_metrics.confusion_matrix(test_labels.numpy(), test_classes.numpy())
    confusion_normalized = confusion / confusion.sum(axis=1, keepdims=True)
    axis_labels = range(10)
    ax = sns.heatmap(
        confusion_normalized, xticklabels=axis_labels, yticklabels=axis_labels,
        cmap='Blues', annot=True, fmt='.4f', square=True)
    plt.title("Матрица ошибок")
    plt.ylabel("Истинные метки")
    plt.xlabel("Предсказанные метки")
    plt.show()

show_confusion_matrix(y_test, test_classes)
