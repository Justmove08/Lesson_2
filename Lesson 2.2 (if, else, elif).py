# # Конструкция IF (если)
# if 0:
#     print('true')
# print('continue')

# # Конструкуия IF-ELSE (если, иначе)
# if 0:
#     print('true')
# else:
#     print('false')

# # Конструкция IF-ELIF
# if 1:
#     print('true')
# elif 1:
#     print('elif_1')
# elif 1:
#     print('elif_2')
# elif 1:
#     print('elif_3')
# else:
#     print('false')

# IF-ELSE для присваивания
# X = 1
# Y = 3
# Z = 5
# # if X:
# #     A = Y
# # else:
# #     A = Z
# # print(A, type(A))
# A = Y if X else Z
# print(A, type(A))

# Практическая задача про автомобиль
brand = 'volvo' # бренд
engine_volume = 1.5 # объем двигателя
horsepower = 151 # мощность двигателя
sunroof = False # наличие люка

# # Проверка условия IF
# if horsepower < 80:
#     print('No tax')

# #Проверка условия IF-ELSE
# if horsepower == 80:
#     print('No tax')
#     print('No tax')
#     print('No tax')
# else:
#     print('Tax')

# Проверка условия IF/ELIF/ELIF/ELSE
tax = 0
if horsepower < 80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 15000
else:
    tax = 50000
print(tax)

# Проверка условия IF для присваивания
cool_car = 0
cool_car = 1 if sunroof == 1 else 0
print(cool_car)