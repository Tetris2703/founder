from math import tan, pi

s = float(input('Введите длину сторон: '))
n = int(input('Введите число сторон: '))

area = (n * s ** 2) / (4 * tan(pi / n))

print(f'Площадь правильного многоугольника: {area}')
