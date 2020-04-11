'''
# Ввод
name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
print('Вас зовут:', name, surname)
age = input('Сколько вам лет? Напишите ответ: ')
print('Ясно, продолжайте изучать урок')

print('Тип переменной "Name":',type(name))
print('Тип переменной "Age":', type(age))
'''

'''
# Операция по приведению типа
age = '29'
int(age)
print(type(age))
print(type(int(age)))

number = 28
kek = str(number)
print(type(number))
print(type(str(number)))
print('Тип переменной "Kek":', type(kek))
'''

'''
# Математические операции
a = input('Введите первое число: ')
b = input('Введите второе число: ')
a = int(a)
b = int(b)

print('Сложение: ',a + b)
print('Умножение: ',a * b)
print('Деление: ',a / b)
print('Возведение в степень: ',a ** b)
print('Целочисленное деление (без выведение результата после запятой): ', a // b)
print('Остаток от деления (деления в столбик)', a % b)

result = (a / b)
print('Тип результата деления: ', type(result))
result_2 = (a % b)
print('Тип результата остатка от деления: ',type(result_2))
result_3 = (a * b)
print('Тип результата умножения: ', type(result_3))
result_4 = (a // b)
print('Тип результата целочисленного деления: ', type(result_4))
'''

#Логические операции
a = True
b = False
print('Существуют переменные "a" и "b"')
print('Логическое значение переменной "a":', a)
print('Логическое значение переменной "b"', b)
# Отрицание
print('Отрицание "not a":', not a)
print('Отрицание "not b":',not b)
# Логическое И
print('Логическое И (a and b): ', a and b)
print('Логическое И (b and a): ', b and a)
# Логическое ИЛИ
print('Логическое ИЛИ (a or b): ', a or b)
print('Логическое ИЛИ (b or a): ', b or a)
print()
a = 10
print('a = 10', a)
print('Правда ли, что a > 100: ', a > 100)
print('Правда ли, что a < 100: ', a < 100)
print('Правда ли, что a <= 100: ', a <= 100)
print('Правда ли, что a >= 100: ', a >= 100)
print('Правда ли, что a == 100: ', a == 100)
print('Правда ли, что a !=  100: ', a != 100)
