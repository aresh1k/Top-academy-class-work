# name = "Roman"  # Имя
# print("Hello", name)
# age = 20
# print(age)
# print(type(age))
# print(id(age))
# age = "hello"
# print(age)
# print(type(age))
#
# a = b = c = 1
# print(a, b, c)
#
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# a = "5"
# b = 2
# print(int(a) + b)
#
# a = 1
# b = 2
# print("a =", a)
# print("b =", b)
#
# c = a
# a = b
# b = c
#
# a = a + b
# b = a - b
# a = a - b
#
# a, b = b, a

# print("строка \
# символов")
# print('строка символовстрока символовстрока символовстрока символовстрока символовстрока символовстрока символовстрока '
#       'символовстрока символовстрока символовстрока символов')
# print('строка \nсимволов')
# print('строка \rсимволов')
# print("\tДокумент       \"file.txt\" D:\\folder\\file.py")
#
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "!\t\t"
# print(s3)
# print(s3 * 3)

# print(54546548946551651231232)
# print(5.454654894655165123123)
#
# print(7 + 2)
# print(7 - 2)
# print(7 * 2)
# print(7 / 2)
# print(7 // 2)
# print(7 ** 2)
# print(7 % 2)

# number = 1 + 2 * 5 ** 2 + 7
# print(number)
# number = (1 + 2) * 5 ** (2 + 7)
# print(number)

# a = 5
# b = 7
# c = 3
# print("Сумма:", a + b + c)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", (a + b + c)/3)


# number = 9753
# a = number % 10
# print(a)
# number = number // 10
# b = number % 10
# print(b)
# number = number // 10
# c = number % 10
# print(c)
# number = number // 10
# d = number % 10
# print(d)
# print(a*1000+b*100+c*10+d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)


# Функции явного преобразования типов
# str()
# int()
# float()
# bool()

# num1 = "2"
# num2 = 3
# res = num1 + str(num2)
# print(res)
#
# print(int(3.8))
# print(round(3.891))


# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут ", name, ". Мне", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Я учу Python.", end="\n\n")

# name = input("Ваше имя: ")
# print(name)

# number = int(input("Введите число: "))
# stepen = int(input("Введите степень: "))
# print("Число", number, "в степени", stepen, "равно", number**stepen)

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)
# print(bool("Python"))   # True
# print(bool(""))     # False
# print(bool(5))  # True
# print(bool(0))  # False
# print(bool(None))   # False
# print(bool(False))  # False


# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возвраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ на сайт запрещен")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a = b")
# else:
#     print("b > a")


# first_side = int(input("Введите значение первой стороны: "))
# second_side = int(input("Введите значение второй стороны: "))
# third_side = int(input("Введите значение третьей стороны: "))
# if first_side == second_side == third_side:
#     print("Треугольник равносторонний")
# elif first_side == second_side or second_side == third_side or first_side == third_side:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if (day >= 1) and (day <= 5):       # 1 <= day <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# month = int(input("Введите номер месяца "))
# if 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# elif month == 12 or month == 1 or month == 2:
#     print("Зима")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Некорректное значение")

# password = "moderator"
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print("Пароль не верен")

# day = 'суббота'
# time = 10
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")
#
# a, b = 10, 20
#
# minin = a if a < b else b
# print(minim)


# a, b = 10, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 10, 0
# print(a/b if b != 0 else "На ноль делить нельзя")


# исключения

# try:
#     n = int(input("Введите целое число: "))
#     print(n*2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки и делить на ноль")
# else:
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# Циклы

# i = 2
# while i < 21:
#     print("i =", i)
#     i += 2

# try:
#     x = int(input('Количество: '))
#     while x > 0:
#         print('*', end='')
#         x -= 1
# except ValueError:
#     print('Введите число!')

# x = int(input("Введите начало диапазона: "))
# y = int(input("Введите конец диапазона: "))
# i = x
# summator = 0
# while i < y:
#     if i % 2 == 1:
#         summator += i
#     i += 1
# print(summator)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# summator = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     summator *= n
# print("Произведение чисел равно", summator)


# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t", end="")
#         j += 1
#     print()
#     i += 1


# for element in collection:
#   тело цикла

# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)
# print(range(5))
#
# # range(start, stop, step)
#
# for i in range(5):
#     print(i)
#
# while i < 100:
#     print(i, end=" ")
#     i += 5

# a = int(input("Введите целое число: "))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i)

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i)

# for i in range(3):
#     print(i, end=" ")
# else:
#     print("\ndone")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if 0 < i < h - 1 and 0 < j < w - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()
#
# letter = [i for i in "Hello"]
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки (list)

# nums = [8, 3, 9, 4, 1, "Hello", 2.3]
# print(nums)
# print(type(nums))
#
# print(nums[0])
# print(nums[-1])
#
# nums[-2] = 2
# print(len(nums))

# s = []
# print(s)
# b = list()
# print(b)
#
# c = list("Hello")
# print(c)

# s = [5, 2] * 6
# print(s)
#
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
#
# print(c)

# n = list(range(10))
# print(n)

# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# n = 5
# a = [i ** 3 for i in "Hello"]
# print(a)


# a = [0] * int(input("Количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("Количество элементов списка: ")))]
# print(a)

# nums = [8, 3, 9, 4, 1]
# print(nums * 2)
# for i in range(len(nums)):
#     print(nums[i], end=" ")
# print()
# for i in nums:
#     print(i ** 2, end=" ")


# a = [int(input("-> ")) for i in range(int(input("Количество элементов списка: ")))]
# summator = 0
# for i in a:
#     if i < 0:
#         summator += i
# print(summator)


# a = list(range(21, 41))
# print(a)
# print()
# b = [i for i in range(21, 41)]
# print(b)

# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         odd += 1
#     else:
#         even += i
# print("Количество четных: ", odd, "\nСумма нечетных ", even)


# a = [int(input("-> ")) for i in range(int(input("Количество элементов списка: ")))]
#
# b = 0
# summa = 0
#
# for i in a:
#     if i != 0:
#         summa += i
#         b += 1
#
# print(summa/b)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов списка: ")))]
#
# b = a[0]
#
# for i in a:
#     if i > b:
#         print(i, end=" ")
#     b = i


# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)
#
#
# # список[start:stop:step]
#
# a = [9, 4, 3, 1, 5, 17]
#
# print(a[1:4])
# print(a[1:])
# print(a[:])


# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[0:1])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])

# a = list(range(1, 8))
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# a[3:5] = []
# print(a)
# del a[0]
# print(a)
# del a[0:3]
# print(a)
# del a[:]
# print(a)


# Методы списков
# print(dir(list))

# a = list(range(1, 8))
# print(a)
# a.append(99)    # добавляет элемент в конец списка
# print(a)
# a.extend([22, 11, 9])   # добавляет множество элементов в конец списка
# print(a)
# a.insert(0, 100)
# print(a)
# a.insert(-1, 100)   # добавляет элемент списка по заданному индексу (за исключением последнего)
# print(a)
# a.extend("add")
# print(a)


# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)


# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("-> "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)


# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)


# first = [1, 2, 3]
# second = [11, 22, 33]
# third = []
# for i in first:
#     for j in second:
#         third.extend([i, j])
#
# print(third)


# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []

# if len(b) < len(a):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])


# b = [11, 12, 13, 2, 4, 13]
# b.remove(13)    # удаляет первый найденный элемент в списке по заданному значению
# print(b)
# a = 0
# if a in b:
#     b.remove(a)
# print(b)
#
# last = b.pop(1)  # с пустыми скобками удаляет последний элемент из списка, с заданным значением удаляет значение по индексу
# print(b)
#
# print(last)
#
# b.clear()   # очищает список
# print(b)


# k = int(input("Количество элементов списка: "))
# n = int(input("Индекс элемента списка: "))
# s = []
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# s.pop(k)
# print(s)

# a = [9, 2, 7, 2, 4, 2, 3]
# print(a)
# print(a.count(2))   # Посчитать количество указанных элементов в списке
#
# ind = a.index(9, 2, -1)    # Возвращает индекс первого встреченного указанного элемента с самого начала или в указанном диапазоне
# print(ind)

# a = [9, 2, 7, 2, 4, 2, 3]
# b = a.copy()
#
# print("a:", id(a))
# print("b:", id(b))
# a.append(20)
# print("a:", a)
# print("b:", b)

# a = [9, 2, 7, 2, 4, 2, 3]
# print(a)
# a.reverse() # разворачивает список
# print(a)
#
# a.sort()    # сортирует список, по умолчанию - по возрастанию
# print(a)
#
# a.sort(reverse=True) # сортировка по убыванию
#
# b = ["Виталий", "Сергей", "Александр", "Анна"]
# print(b)
# b.sort(key=len)
# print(b)

# a = [9, 2, 7, 2, 4, 2, 3]
# c = sorted(a)
# print(c)


# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(2, 9))     # генерация случайного целого значения в заданном диапазоне включая конец списка
#
# print(random.randrange(1, 9, 2))      # генерация случайного целого числа в заданном диапазоне с заданным шагом не включая конец списка


# from random import randint, randrange
#
# print(randint(2, 9))


# from random import *

# print(randint(2, 9))

# import random as rd

# print(rd.randint(2, 9))

# import random as r
#
# print(r.randint(2, 9))
# print(r.randrange(1, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 3))
#
# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(r.choice(city))
# print(r.choices(city, k=3))
#
# r.shuffle(city)
# print(city)

# import random as r

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))
# print(sum(lst))

# sum = [5, 3, 2, 4, 1]
#
# a = [1, 2, 3]
# print(max(sum))
# print(sum(sum))
# print(sum(a))

# b = []
# b.pop()


# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
#
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
#
# print(res)


# x = list("1a2b3c4c")
#
# print(x)
#
# print("a" in x)
# print("w" in x)
#
# print("w" not in x)
#
# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("Список пустой")

# from random import randint
#
# n1 = int(input("Количество элементов первого списка: "))
# n2 = int(input("Количество элементов второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
#
# c = a + b
# print("Третий список (сложение списков): ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(a[i])
# print("Третий список без повторений: ", c)
#
#
# c = []
#
# for i in range(len(a)):
#     if a[i] not in b and a[i] not in c:
#         c.append(a[i])
#
# print("Третий список c общими элементами: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
#
# print(c)


# from random import randint
#
# n = int(input("Количество элементов списка: "))
# a = [randint(0, n - 1)]
# while len(a) < n:
#     c = randint(0, n - 1)
#     if c not in a:
#         a.append(c)
# print(a)

# m = [
#     [1, 2, 3, 4]
#     [5, 6, 7, 8]
#     [9, 10, 11, 12]
# ]
#
# print(m)
# print(m[2][2])
#
# for row in range(len(m)):
#     for col in range(len(row)):
#         print(m[row][col], end="\t")
#     print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()


# w, h = 5, 3
# matrix = []
#
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# print([[x for x in row] for row in matrix])


# for x, y in [[1, 2], [3,4], [5, 6], [7,8]]:
#     print(x, "+", y, "=", x + y)


# from random import randrange
#
# w, h = 3, 4
# matrix = [[randrange(-20, 10) for x in range(w)] for y in range(h)]
#
# i = 0
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             i += 1
#     print()
# print("Количество отрицательных элементов: ", i)


# from random import randrange
#
# w, h = 3, 4
# matrix = [[randrange(0, 4) for x in range(w)] for y in range(h)]
#
# i = 1
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#         if x > 0:
#             i = i * x
#     print()
# print("Произведение ненулевых чисел: ", i)


# from random import randint
#
# w = h = 6
# n = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# s = []
# for i in range(w):
#     if matrix[i][i]:
#         s.append()


# import math


# num1 = math.sqrt(4)
# print(num1)
#
# num2 = math.ceil(3.2)
# print(num2)
#
# num3 = math.floor(3.8)
# print(num3)

# print(round(int(input("Введите радиус окружности: "))*2*math.pi, 2))


# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")

# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime(4641341864)
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(4654414541)))
#
# pause = 5
# print("Программа запустилась")
# time.sleep(pause)
# print(pause, "seconds")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "sec.")


# Функции


# def hello(name, word):
#     print("Hello, ", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")


# def get_sum(a, b):
#     x = 1
#     print(x)
#     print(a + b)
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("x", "y")
# get_sum(2.5, 4.7)


# def symbol(count, a, b):
#     print((a + b) * (count // 2) + a * (count % 2))
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# if maximum(5, 3):
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Этот пароль надежный")
# else:
#     print("Это ненадежный пароль")


# def cube(x):
#     return x**3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     a = lst.pop()
#     b = lst.pop(0)
#     lst.insert(0, a)
#     lst.append(b)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info(("Ira", 23))
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
#
#
# print(lt1 == lt2)
# print(lt1 is lt2)
#
#
# a = 5
# b = 5
#
# print(a == b)
# print(a is b)


# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))

# s = "Hello"
# print(id(s))
#
# s += "World"
# print(s)
# print(id(s))


# Кортеж (tuple)


# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = ()
# print(type(a))
#
# b = tuple()
# print(type(b))

# s = tuple(input("-> ") for i in range(3))
# print(s)


# from random import randint
#
# s = tuple(randint(1, 30) for i in range(3))
# print(s)

# b = tuple(2**i for i in range(1, 13))
# print(b)


# def slicer(tpl, el):
#     if tpl.count(el) == 1:
#         return tpl[tpl.index(el):]
#     elif tpl.count(el) > 1:
#         a = tpl.index(el)
#         b = tpl.index(el, a + 1) + 1
#         return tpl[a:b]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randrange
#
#
# def tuple_generator(x, y):
#     return tuple(randrange(x, y) for i in range(10))
#
#
# a = tuple_generator(0, 5) + tuple_generator(-5, 0)
#
# print(a)
# print(a.count(0))


# point = (10, 0)
#
# match point:
#     case (0, 0):
#         print("Точка находится в координатах 0:0")
#     case (x, 0):
#         print("Точка находится в координате", x, "по оси Х и в координате 0 по оси Y")
#     case (0, y):
#         print("Точка находится в координате 0 по оси Х и в координате", y, "по оси Y")
#     case (x, y):
#         print("Точка находится в координате", x, "по оси Х и в координате", y, "по оси Y")
#     case _:
#         print("Это не координаты точки")


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# name1, age1, married1 = user
# print(user)
# print(name1, age1, married1)
#
#
# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst = list(tpl)
# print(lst)
#
#
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
# print()
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     # print(country)
#     print("\nСтрана:", countryName, "население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)

# set() - множество

# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)
# print(type(s))
# print(len(s))

# c = ['red', 'green', 'green', 'blue']
# a = set('hello')
# print(type(a))
# print(a)
# a = set(c)
# print(a)
#
#
# s = {x * x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)


# def to_set(some_list):
#     a = set(some_list)
#     return a, len(a)
#
# a = "я обычная строка"
# b = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
#
# print(to_set(a))
# print(to_set(b))

# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
# print('apple' not in s)
# print(s)
# for i in s:
#     print(i)


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# c = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == "c"}
# print(a)
# print(b)
# print(c)


# s = {"banana", "apple", "orange"}
# s.add(4)
# print(s)
# if 4 in s:
#     s.remove(4)
# s.discard(4)    # удаляет элемент по значению без генерации ислючения
# print(s)
#
# s.pop()
# print(s)
# s.clear()
# print(s)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# c = a | b
# print(c)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))


# s1 = "Hello"
# s2 = "How are you"
# print(set(s1) & set(s2))
# a = set(s1) & set(s2)
# for i in a:
#     print(i, end=" ")


# s1 = "Python"
# s2 = "Programming language"
# print(set(s1).difference(s2))


# drawing = {"Марина", "Света", "Женя"}
# music = {"Костя", "Женя", "Илья"}
#
# one_hobby = drawing ^ music
# both_hobby = drawing & music
# print(one_hobby)
# print(both_hobby)
# drawing = drawing - music
# print(drawing)


# frozenset()

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# s1 = frozenset({"hello", "world"})
# print(s1)
#
#
# s1.add()


# Словарь (dict)

# a = [1, 2, 3]
# d = {1: 'one', 'two': 2, 'three': 3, 'four': 3}
# print(a[0])
# print(d['one'])
# print(d[1])
#
#
# d = {}
# print(d)
# print(type(d))


# d = dict()
# print(d)
# print(type(d))

# d = {"one": 1, "two": 2}
# d = dict(one=1, two=2)
# print(d)
# print(type(d))


# a = [
#     ("igor@gmail.com", "Igor"),
#     ("irina@gmail.com", "Irina"),
#     ("anna@gmail.com", "Anna")
# ]
#
# b = dict(a)
# print(b)


# d = {i: i ** 2 for i in range(2, 7)}
# print(d)
# print(d[3])
# d[3] = 15
# print(d)


# d = {0: "text", "one": 45, (1, 2.3): "Кортеж", (2, 3, 6, 7): 42, True: {1, 0}}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)])
# d[(1, 2.3)] = "Новое значение"
# print(d)
# print("one" in d)
# print(d["one1"])
#
# key = 'one'
# # if key in d:
# #     del d[key]
# # print(d["one1"])
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + "нет в словаре")
#
# print(d)

# d = {0: "text", "one": 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
#
# for key in d:
#     print(key, "-> ", d[key])


# some_dict = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# summator = 1
# for key in some_dict:
#     summator *= some_dict[key]
# print(summator)


# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)
# d = {i: input("-> ") for i in range(1, 5)}
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != "0":
#         qty = int(input("Количество: "))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по", goods[i][2], "руб", sep="")


# d = {"a": 1, "b": 2, "c": 3}
# print(d["b"])
# value = d.get("f", "Такого ключа не существует")    # Получить значение по заданному ключу
# print(value)
# n = d.keys()    # Получить список ключей
# print(n)
# n = d.values()  # Получить список значений
# print(n)
# n = d.items()   # Список кортежей, в которые входят ключ + значение
# print(n)
#
# for i in d:
#     print(i)
#
# for i in d.keys():
#     print(i)
#
# for i in d.values():
#     print(i)
#
# for i, j in d.items():
#     print(i, "->", j)


# d = {"a": 1, "b": 2, "c": 3}
#
# d2 = d.copy()   # Создание копии словаря
#
# print("D =", d)
# print("D2 =", d2)
#
# d["b"] = 5
# d2["e"] = 7
#
# print("D =", d)
# print("D2 =", d2)


# d = {"a": 1, "b": 2, "c": 3}
# item = d.pop("b")   # удаляет элемент из словаря по ключу, возвращает значение ключа
# print(item)
# print(d)
# item = d.popitem()  # удаляет произвольную пару ключ + значение и возвращает их
# print(d)

# item = d.setdefault("f", 5)     # добавляет ключ со значением по умолчанию, если ключа не существует
# print(item)
# print(d)


# d.update{"a": 20, "w": 10}
# print(d)

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
# print(new_d)
# print(d)


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# d["location"] = d.pop("city")
# print(d)


# a = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three",
#     },
#     "second": {
#         4: "fourth",
#         5: "five"
#     }
# }
#
# print(a)
#
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")


# sales = {
#     "John": {
#         "N": 3056,
#         "S": 8463,
#         "E": 8441,
#         "W": 2694,
#     },
#     "Tom": {
#         "N": 4832,
#         "S": 6786,
#         "E": 4737,
#         "W": 3612,
#     },
#     "Anne": {
#         "N": 5239,
#         "S": 4802,
#         "E": 5820,
#         "W": 1859,
#     },
#     "Fiona": {
#         "N": 3904,
#         "S": 3645,
#         "E": 8821,
#         "W": 2451,
#     }
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
#
# name = input("Введите имя: ")
# region = input("Введите регион: ")
# new_sales = int(input("Введите новый объем продаж: "))
# sales[name][region] = new_sales
#
# print(sales[name])


# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# w = {k: v for k, v in d.items()}
# print(w)


# value = int(input("-> "))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)


# d = {"a": 1, "b": 2, "c": 3, "d": 4}
#
# value = list(d)
# print(value)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     some_list = list()
#     if type(i) == str:
#         d[i] = []   # d["one"] = []
#         s = i   # s = "one"
#     else:
#         d[s].append(i)
#
# print(d)


# a = {"Dec", "Jan", "Feb"}
# b = {12, 1, 2}
# d = list(zip(a, b))
# print(d)


# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# c = [2.0, 4.6, 7.5]
# d = list(zip(a, b, c))
# print(d)


# one = {"name": "Igor", "last_name": "Doe", "job": "Consultant"}
# two = {"name": "Irina", "last_name": "Smith", "job": "Manager"}


# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# one = {{"name": "Igor", "last_name": "Doe", "job": "Consultant"},
#        {"name": "Irina", "last_name": "Smith", "job": "Manager"}
#        }
# print(one)

# pairs = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
# a, b = zip(*pairs)
# print(a)
# print(b)


# one = {"apple": 0.4, "orange": 0.35}
# two = {"pepper": 0.2, "onion": 0.55}
# print({**one, **two})


# data = ["a", "b", "c", "d"]

# for i in data:
#     print(i, end=" ")
# print()
# for i in range(len(data)):
#     print(i, end=" ")
#
# j = 1
#
# for i in data:
#     print(j, ":", i)
#     j += 1

# for j, i in enumerate(data, 100):
#     print(j, ":", i)

# n = {"a": 1, "b": 2, "c": 3, "d": 4}
#
# for j, (i, v) in enumerate(n.items(), 100):
#     print(j, ":", i, "->", v)


# a = [1, 2, 3]
# b = [4, *a, 5, 6]
# print(b)
#
#
# def func(*args):
#     res = 0
#     for i in args:
#         res += 1
#     return res
#
#
# print(func(3, 2))
# print(func(3, 4, 6))
# print(func())


# def to_dict(*lst):
#     return {i: i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("gray", (2, 17), 3.11, -4))

# import random
#
#
# def func(*args):
#     average = 0
#     new_list = []
#     for i in args:
#         average += i
#     average = average / len(args)
#     for i in args:
#         if i > average:
#             new_list.append(i)
#     return new_list
#
#
# some_list = [random.randint(1, 10) for i in range(10)]
#
#
# print(func(some_list))


# def func(a, *args):
#     return a, args
#
#
# print(func(2, 3))
# print(func(2, 3, 4, 'abc'))

# def print_scores(student, *scores):
#     print("Student Name:", student, end=", scores: ")
#     a, b = None, ""
#     for score in scores:
#         a = str(score) + ", "
#         b += a
#     print(b[:-2])
#
#
# print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33, 56)


# def reverse_num(n):
#    s = str(n)
#    return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))

# def func(**kwargs):
#     return


# def func(**data):
#     for key, value in data.items():
#         print(key, "is", value)
#     print()
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))
#
#
# func(name="Irina", surname="Sharma", age=22, phone=1234567890)
# func(name="Igor", surname="Wood", email="igor@mail.ru", country="Russia", age=25, phone=98765432100)


# my_dict = {"one": "first"}
#
#
# def db(**kwargs):
#     for key, value in kwargs.items():
#         my_dict[key] = value
#     print(my_dict)
#
#
# db(k1=22, k2=31, k=33, k4=91)


# Области видимости (scope)

# name = "Tom"    # глобальная переменная
# surname = ""
#
#
# def hi():
#     global name, surname
#     name = "Sam"
#     # name = "Sam"    # локальные переменные
#     surname = "Johnson"
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# print(name)
# bye()


# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#     inner_func()
#
#
# outer_func("world!")
#
#
# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()


# x = 25
#
#
# def fn():
#     global t
#     a = 30
#     t = a
#
#
# fn()
# z = x + t
# print(z)


# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print(z)


# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 35
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + b1
#         b = a2 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add = outer(5)
# print(add(10))


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#
#
# print(rect_paral_square(2, 4, 6))


# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res1()


# students = {
#     "Alice": 98,
#     "Bob": 67,
#     "Chris": 85,
#     "David": 75,
#     "Ella": 54,
#     "Fiona": 35,
#     "Grace": 69
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a + b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())


# lambda (Анонимные функции)


# func = lambda x, y: x + y
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)("a", "b"))


# print((lambda x, y: x**2 + y**2)(2, 5))

# summ = lambda a, b=2, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))


# func = lambda *args: args
#
# print(func(1, 2, 3, 4, 5, 6, 7))


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))


# def inc(n):
#     return lambda x: n + x
#
#
# f = inc(42)
# print(f(3))
#
#
# inc1 = (lambda n: lambda x: n + x)
#
#
# def inc2(n):
#     def wrap(x):
#         return n + x
#
#
# f3 = inc1(42)
# print(f3(3))


# players = {
#     {"name": "Антон", "last name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last name": "Бодня", "rating": 10},
#     {"name": "Федоров", "last name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last name": "Семенов", "rating": 6}
# }
#
# res = sorted(players, key=lambda item: item["last name"])
# print(res)
#
# res = sorted(players, key=lambda item: item["rating"])
# print(res)
#
# res = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res)

# d = {"b": 15, "a": 3, "c": 7}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(a[3](12, 3))

# a = {"one": lambda x: x - 1, "two": lambda x: x - 3, "three": lambda x: x}
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a["two"](i))
#     elif i > 0:
#         print(a["one"](i))
#     else:
#         print(a["three"](i))
#
#
# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
#
# d[3]()

# m = lambda: a, b: a if a > b else b
# print(m(12, 5))


# m = lambda a, b, c: a if a < b and a < c else b if b < c else c
# print(m(9, 18, 5))


# map(), filter()

# map(func, iterable), filter(func, iterable)

# def mul(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mul, lst))
# lst2 = list(map(lambda t: t * 2, lst))
#
# print(lst2)

# t = (2.88, -1.75, 100.03)
#
# # t2 = tuple(map(lambda x: int(x)), t)
# t2 = tuple(map(int, t))
#
# print(t2)
#
#
# area = [3.456789, 5.784569, 4.001256, 7.987426, 1.4523689, 8.7412594]
#
# # res = list(map(round, area, range(1, 7)))
# # res = list(map(round, area, range(2, 8)))
# res = list(map(round, area, [2, 2, 2, 2, 2, 2]))
#
#
# print(res)
#
# # print(round(3.45612131, 3))


# st = ["a", "b", "c", "d", "e"]
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)
#
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# filter (func, iterable)


# t = ('abcd', "abd", "adefg", "def", "ghi")
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# import random
# some_list = [random.randint(0, 40) for i in range(10)]
# print(some_list)
# filtered_list = list(filter(lambda i: 10 < i <= 20, some_list))
# print(filtered_list)

# some_list = [45, 55, 60, 37, 100, 105, 220]
# print(some_list)
# filtered_list = list(filter(lambda i: i % 15 == 0, some_list))
# print(filtered_list)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))     #
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)

# Декораторы


# def hello():
#     return "Hello, I am func 'hello'"


# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())

# test = hello

# super_func(hello)
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print("Code before")
#         func()
#         print("Code after")
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):     # декорирующая функция
#
#     def func_wrapper():
#         print("Code before")
#         func()
#         print("Code after")
#     return func_wrapper
#
#
# @my_decorator   # декоратор
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "<b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "<i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Назарова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("Данные:", args)
#         print("Данные:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)
#
#
# print_full_name("Ирина", "Назарова")
# print_full_name_1("Виктор", last="Назаров", second="Федорович")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)


# summa(5, 2)
# sub(5, 2)


# def multiply(num):
#     def decor(func):
#         def wrap(mult):
#             return mult * func(num)
#         return wrap
#     return decor
#
#
# @multiply(3)
# def new_number(num):
#     return num
#
#
# print(new_number(5))


# def typed(*args, **kwargs):
#     def wrapper(func):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных!", f_args[i])   # print("Некорректный тип данных!")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных!", f_args[i])   # print("Некорректный тип данных!")
#
#
#             return func(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World", z=5))


# def args_decorator(tx=None, decorator_text=""):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     return my_decorator
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world2(text):
#     print(text)
#
#
# hello_world("world")
# hello_world2("Hi")


print("Вносим изменения в склонированный проект")


