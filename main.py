# Кастаньо Абе Хосе Луис. 44-22-116. Вариант 4. Задание 3

import math as m


def function_(x):
    if x <= 1.6:
        return (x**2 + m.cos(x))
    else:
        assert x > 1.6, "x must be positive"
        return (x - m.sin(0.2*x))

try:
    x = int(input("Введите число: "))
    print(function_(x))

except ValueError as err:
    print("Будьте внимательны:", err)
