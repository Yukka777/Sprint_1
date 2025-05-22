import re

time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

# Разделяем строку на отдельные временные значения
time_values = re.split(r",|\s", time_string)

for value in time_values:
    if not value: # Пропускаем пустые строки, которые могли получиться после split
        continue

    hours = 0
    minutes = 0
    seconds = 0

    if 'h' in value:
        hours = int(value.replace('h', ''))
    if 'm' in value:
        minutes = int(value.replace('m', ''))
    if 's' in value:
        seconds = int(value.replace('s', ''))

    total_minutes += (hours * 60) + minutes + (seconds // 60)

print(total_minutes)
