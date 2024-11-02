SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60
SECONDS_PER_DAY = SECONDS_PER_HOUR * 24

total = int(input('Введите кол-во cекунд для перевода: '))

days = total // SECONDS_PER_DAY
remaining = total % SECONDS_PER_DAY

hours = remaining // SECONDS_PER_HOUR
remaining = remaining % SECONDS_PER_HOUR

minutes = remaining // SECONDS_PER_MINUTE
seconds = remaining % SECONDS_PER_MINUTE

print(f'Длительность: {days} {hours:02d}:{minutes:02d}:{seconds:02d}')