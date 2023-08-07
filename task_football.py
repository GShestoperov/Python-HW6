# Задача FOOTBALL необязательная

# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Пример входа:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Выход будет:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


# ввод исходных данных
def input_matches() -> list[list[str, int, str, int]]:
    # matches_list = [
    #     ["Спартак", 9, "Зенит", 10],
    #     ["Локомотив", 12, "Зенит", 3],
    #     ["Спартак", 8, "Локомотив", 15],
    # ]
    nn = int(input("Введите количество игр: "))
    matches_list = []
    for i in range(nn):
        input_str = input(
            f"Введите игру {i+1} в формате 'Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой': "
        )
        input_list = input_str.split(";")
        matches_list.append(
            [
                input_list[0],
                int(input_list[1]),
                input_list[2],
                int(input_list[3]),
            ]
        )
    return matches_list


# расчет турнирной таблицы
def generate_tournament_table(
    matches_list: list[list[str, int, str, int]]
) -> dict[str : list[int, int, int, int, int]]:
    win_count = 0
    draw_count = 0
    loss_count = 0
    current_score = 0
    res = {}
    for item in matches_list:
        # код для первой команды
        if item[1] > item[3]:
            win_count = 1
            draw_count = 0
            loss_count = 0
            current_score = 3
        elif item[1] == item[3]:
            win_count = 0
            draw_count = 1
            loss_count = 0
            current_score = 1
        else:
            win_count = 0
            draw_count = 0
            loss_count = 1
            current_score = 0

        if item[0] in res:
            res[item[0]] = [
                res[item[0]][0] + 1,
                res[item[0]][1] + win_count,
                res[item[0]][2] + draw_count,
                res[item[0]][3] + loss_count,
                res[item[0]][4] + current_score,
            ]
        else:
            res[item[0]] = [
                1,
                win_count,
                draw_count,
                loss_count,
                current_score,
            ]

        # код для второй команды
        if item[3] > item[1]:
            win_count = 1
            draw_count = 0
            loss_count = 0
            current_score = 3
        elif item[3] == item[1]:
            win_count = 0
            draw_count = 1
            loss_count = 0
            current_score = 1
        else:
            win_count = 0
            draw_count = 0
            loss_count = 1
            current_score = 0

        if item[2] in res:
            res[item[2]] = [
                res[item[2]][0] + 1,
                res[item[2]][1] + win_count,
                res[item[2]][2] + draw_count,
                res[item[2]][3] + loss_count,
                res[item[2]][4] + current_score,
            ]
        else:
            res[item[2]] = [
                1,
                win_count,
                draw_count,
                loss_count,
                current_score,
            ]

    return res


# вывод турнирной таблицы
def print_tournament_table(tournament_table: dict[str:[int, int, int, int, int]]):
    print("Турнирная таблица:")
    for key, item in tournament_table.items():
        print(f"{key}: {item[0]} {item[1]} {item[2]} {item[3]} {item[4]}")


matches_list: list[list[str, int, str, int]] = input_matches()
print(matches_list)
tournament_table: dict[str : list[int, int, int, int, int]] = generate_tournament_table(
    matches_list
)
print_tournament_table(tournament_table)
