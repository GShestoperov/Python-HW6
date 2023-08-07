# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.


def generate_arithmetical(a1: int, d: int, n: int) -> list[int]:
    arithmetical_list = []
    for i in range(n):
        arithmetical_list.append(a1 + d * i)
    return arithmetical_list


a1 = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите разность элементов: "))
n = int(input("Введите количество элементов: "))

print(f"Ваша арифметическая прогрессия: {generate_arithmetical(a1, d, n)}")
