# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

numbers = []
for number in range(1, 101):
    numbers.append(number)
    new_str = str(number)
    new_list = list(new_str)
    # print(new_list)
    # print(new_list[-1])
    if int(new_list[-1]) == 1 and number != 11:
        print(f'{number} процент')
    elif 2 <= int(new_list[-1]) <= 4:
        if number < 5:
            print(f'{number} процента')
        elif number > 14:
            print(f'{number} процента')
    else:
        print(f'{number} процентов')
