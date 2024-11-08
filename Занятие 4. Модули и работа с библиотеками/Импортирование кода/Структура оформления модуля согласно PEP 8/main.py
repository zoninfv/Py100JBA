"""Модуль для вычисления площади квадрата"""

import math

SIDE_LENGTH = 5


def calculate_area(side_length):
    """Вычисляет площадь квадрата."""
    return math.pow(side_length, 2)


if __name__ == '__main__':
    area = calculate_area(SIDE_LENGTH)
    print(f"Площадь квадрата со стороной {SIDE_LENGTH} равна {area}")
