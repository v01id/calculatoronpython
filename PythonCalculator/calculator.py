print('Введите первое число: ')
a = float(input())
print('Введите второе число: ')
b = float(input())

print('\t\t\tВыберете математическую операцию\t')
print('1 - Сложение')
print('2 - Вычитание')
print('3 - Умножение')
print('4 - Деление')
print('5 - Возведение в степень')
print('6 - Остаток от деления')
print('7 - Получение целой части от деления')

select = float(input())

if select == 1:
    print('Сумма чисел сложения: ', a + b)

elif select == 2:
    print('Сумма чисел вычитания: ', a - b)

elif select == 3:
    print('Сумма чисел умножения: ', a * b)

elif select == 4:
    print('Сумма чисел деления: ', a / b)

elif select == 5:
    print('Сумма чисел возведения в степень: ', a ** b)

elif select == 6:
    print('Сумма остатка от деления: ', a % b)

elif select == 7:
    print('Сумма получения целой части от деления: ', a // b)

input()