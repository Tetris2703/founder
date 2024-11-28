"""
Декоратор @tf.function в TensorFlow используется для преобразования функции Python в граф вычислений TensorFlow.
Это приводит к нескольким преимуществам, которые могут объяснить, почему функции,
помеченные этим декоратором, работают быстрее.

Вот основные причины:
1. Компиляция в граф:
2. Устранение накладных расходов Python:
3. Оптимизация под аппаратное обеспечение:
4. Кэширование графа:
5. Улучшенная оптимизация операций:

В результате использования @tf.function вы получаете более быстрое
выполнение за счет уменьшения накладных расходов на интерпретацию,
улучшенной оптимизации и использования возможностей графа вычислений.
"""


import tensorflow as tf
import numpy as np
import time

# Создаем тестовые данные
A = np.random.rand(1000, 1000).astype(np.float32)
B = np.random.rand(1000, 1000).astype(np.float32)

# Функция без декоратора @tf.function
def matrix_multiply_no_tf_function(A, B):
    return tf.matmul(A, B)

# Функция с декоратором @tf.function
@tf.function
def matrix_multiply_with_tf_function(A, B):
    return tf.matmul(A, B)

# Измеряем время выполнения первой функции
start_time = time.time()
result_no_tf_function = matrix_multiply_no_tf_function(A, B)
end_time = time.time()
print(f"Время выполнения без @tf.function: {end_time - start_time:.6f} секунд")

# Измеряем время выполнения второй функции
start_time = time.time()
result_with_tf_function = matrix_multiply_with_tf_function(A, B)
end_time = time.time()
print(f"Время выполнения с @tf.function: {end_time - start_time:.6f} секунд")

# Проверка на равенство результатов
print("Результаты равны:", np.allclose(result_no_tf_function.numpy(), result_with_tf_function.numpy()))
