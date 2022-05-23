# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

duration = int(input("Введите число: "))
days = duration // 86400
hours = (duration % 86400) // 3600
minutes = ((duration % 86400) % 3600) // 60
seconds = (((duration % 86400) % 3600) % 60)
print(f'{days} days {hours} hours {minutes} minutes {seconds} seconds')





