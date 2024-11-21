import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Загрузка данных
data = pd.read_csv('SBER.csv', sep=';')
data.columns = ['DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']
data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d')
data.set_index('DATE', inplace=True)

# Параметры для полос Боллинджера
period = 20  # Период SMA
bol_size = 2  # Ширина коридора

# Расчет SMA и стандартного отклонения
data['SMA'] = data['CLOSE'].rolling(window=period).mean()
data['STD'] = data['CLOSE'].rolling(window=period).std()

# Расчет верхней и нижней полосы Боллинджера
data['Upper_Band'] = data['SMA'] + (data['STD'] * bol_size)
data['Lower_Band'] = data['SMA'] - (data['STD'] * bol_size)

# Удаление NaN значений
data.dropna(inplace=True)

# Расчет SMA 5 и SMA 20
data['SMA_5'] = data['CLOSE'].rolling(window=5).mean()
data['SMA_20'] = data['CLOSE'].rolling(window=20).mean()

# Расчет RSI
def RSI(df, n=14):
    close = df['CLOSE']
    delta = close.diff()
    delta = delta[1:]
    pricesUp = delta.copy()
    pricesDown = delta.copy()
    pricesUp[pricesUp < 0] = 0
    pricesDown[pricesDown > 0] = 0
    rollUp = pricesUp.rolling(n).mean()
    rollDown = pricesDown.abs().rolling(n).mean()
    rs = rollUp / rollDown
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi

# Вынесем настройки в отдельную функцию
def button_add(figure):
    figure.update_xaxes(rangeslider_visible=True, rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=1, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    ),
                      rangeslider_thickness=0.1  # Уменьшаем высоту слайдера
                      )

data['RSI'] = RSI(data)

# Расчет MACD и сигнала к сделке
EMA_12 = data['CLOSE'].ewm(span=12, adjust=False).mean()
EMA_26 = data['CLOSE'].ewm(span=26, adjust=False).mean()
data['MACD'] = EMA_12 - EMA_26
data['MACD_signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

# График 1: Полосы Боллинджера и SMA
fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=data.index, y=data['CLOSE'], mode='lines', name='Цена закрытия', line=dict(width=2)))
fig1.add_trace(go.Scatter(x=data.index, y=data['SMA'], mode='lines', name='SMA', line=dict(width=2, color='orange')))
fig1.add_trace(go.Scatter(x=data.index, y=data['Upper_Band'], mode='lines', name='Верхняя полоса', line=dict(dash='dash', color='rgba(128, 128, 128, 0.5)')))
fig1.add_trace(go.Scatter(x=data.index, y=data['Lower_Band'], mode='lines', name='Нижняя полоса', line=dict(dash='dash', color='rgba(128, 128, 128, 0.5)')))

fig1.update_layout(
    title='Полосы Боллинджера и SMA',
    xaxis_title='Дата',
    yaxis_title='Цена',
    template='plotly',
    legend=dict(x=0.01, y=0.99),
    height=900,  # Уменьшаем высоту графика
    yaxis=dict(range=[240, 280])  # Минимум и максимум оси Y
)



# График 2: SMA 5 и SMA 20
fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=data.index, y=data['SMA_5'], mode='lines', name='SMA 5', line=dict(width=2, color='blue')))
fig2.add_trace(go.Scatter(x=data.index, y=data['SMA_20'], mode='lines', name='SMA 20', line=dict(width=2, color='green')))

fig2.update_layout(
    title='SMA 5 и SMA 20',
    xaxis_title='Дата',
    yaxis_title='Цена',
    template='plotly',
    legend=dict(x=0.01, y=0.99),
    height=900,  # Уменьшаем высоту графика
    yaxis=dict(range=[240, 280])  # Минимум и максимум оси Y
)


# График 3: RSI и две горизонтальные полупрозрачные линии на значениях 30 и 70
fig3 = go.Figure()

fig3.add_trace(go.Scatter(x=data.index, y=data['RSI'], mode='lines', name='RSI', line=dict(width=2, color='purple')))
fig3.add_shape(type="line", x0=data.index.min(), y0=30, x1=data.index.max(), y1=30, line=dict(color="red", dash="dash"))
fig3.add_shape(type="line", x0=data.index.min(), y0=70, x1=data.index.max(), y1=70, line=dict(color="red", dash="dash"))

fig3.update_layout(
    title='RSI',
    xaxis_title='Дата',
    yaxis_title='RSI',
    template='plotly',
    legend=dict(x=0.01, y=0.99),
    height=900,  # Уменьшаем высоту графика
    yaxis=dict(range=[0, 100])  # Минимум и максимум оси Y
)



# График 4: MACD и MACD_signal
fig4 = go.Figure()

fig4.add_trace(go.Scatter(x=data.index, y=data['MACD'], mode='lines', name='MACD', line=dict(width=2, color='blue')))
fig4.add_trace(go.Scatter(x=data.index, y=data['MACD_signal'], mode='lines', name='MACD_signal', line=dict(width=2, color='orange')))

fig4.update_layout(
    title='MACD и MACD_signal',
    xaxis_title='Дата',
    yaxis_title='MACD',
    template='plotly',
    legend=dict(x=0.01, y=0.99),
    height=900,  # Уменьшаем высоту графика
    yaxis=dict(range=[-3, 7])  # Минимум и максимум оси Y
)

for fig in [fig1, fig2, fig3, fig4]:
    button_add(fig)


# Показать графики
fig1.show()
fig2.show()
fig3.show()
fig4.show()
