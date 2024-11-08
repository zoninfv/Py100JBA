""" Только для python >= 3.9 """


def get_tuple() -> tuple[int, str]:  # кортеж из двух элементов
    return 1, "two"


def get_tuple_ints() -> tuple[int, ...]:  # кортеж произвольной длины
    return 1, 2, 3


def get_list() -> list[int]:  # внутри все значения типа int
    return [1, 2, 3, 4, 5]


def get_dict() -> dict[int, list]:  # пара тип ключа - тип значения
    return {1: [2]}
