souvenir_weight = 75
trinket_weight = 112

souvenir_amount = int(input('Введите кол-во сувениров: '))
trinket_amount = int(input('Введите кол-во безделушек: '))

total_weight = (souvenir_weight * souvenir_amount) + (trinket_weight * trinket_amount)

print(f'Общий вес посылки: {total_weight}г или {total_weight / 1000}кг')