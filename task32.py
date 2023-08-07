# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


def generate_random_list() -> list[int]:
    n = randint(5, 20)
    return [randint(0, 100) for _ in range(n)]


rnd_list = generate_random_list()
print(f"Входной массив: {rnd_list}")

min_value = int(input("Введите минимум: "))
max_value = int(input("Введите максимум: "))

index_list = []
for i, v in enumerate(rnd_list):
    if v >= min_value and v <= max_value:
        index_list.append(i)

print(f"Ваши индексы: {index_list}")
