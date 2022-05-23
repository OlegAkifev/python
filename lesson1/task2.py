#  Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

numbers = []
total_sum = 0

# Генерация чисел от 1 до 1000
for generated_number in range(1, 1001):
    if generated_number % 2 != 0:
        generated_number = generated_number ** 3
        numbers.append(generated_number)
print(numbers)

for elem in numbers:
    first_sum_of_numbers_in_number = 0
    elem = str(elem)
    convert_first = list(elem)
    # print(convert)
    for a in convert_first:
        first_sum_of_numbers_in_number += int(a)
    # print(sum_of_numbers_in_number)
    if first_sum_of_numbers_in_number % 7 == 0:
        total_sum += first_sum_of_numbers_in_number
        # print(first_sum_of_numbers_in_number)
print(total_sum)

total_sum = 0
for i in numbers:
    # print(numbers.index(i))
    # print(numbers[numbers.index(i)])
    numbers[numbers.index(i)] += 17
print(numbers)
for b in numbers:
    second_sum_of_numbers_in_number = 0
    b = str(b)
    convert_second = list(b)
    # print(convert_second)
    for c in convert_second:
        second_sum_of_numbers_in_number += int(c)
        # print(second_sum_of_numbers_in_number)
        if second_sum_of_numbers_in_number % 7 == 0:
            total_sum += second_sum_of_numbers_in_number
            # print(second_sum_of_numbers_in_number)
print(total_sum)
