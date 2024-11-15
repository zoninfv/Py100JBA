# TODO Напишите функцию calculate_average_age
def calculate_average_age(students: list[dict])-> float:
     total_age = sum([student["age"] for student in students])
     averageage = total_age / len(students)
     return averageage
# TODO Напишите функцию filter_students_by_age
def filter_students_by_age (students: list[dict],agefilter: float) -> list[dict]:
    filters = [student["name"] for student in students if student['age'] < agefilter]
    return filters
if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    avage = calculate_average_age(students_list)
    # TODO Вычислите средний возраст учеников
    print("Средний возраст учеников:", avage)

    # Фильтрация учеников по возрасту
    # TODO Офильтруйте учеников
    filtered = filter_students_by_age(students_list,avage)
    # print(filtered)
    print("Список учеников с возрастом меньше среднего:")
    for current_student in filtered:
        print(current_student['name'])
