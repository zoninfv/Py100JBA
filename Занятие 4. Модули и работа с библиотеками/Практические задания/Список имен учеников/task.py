# TODO Напишите функцию get_student_names
def get_student_names(students: list[dict]) -> list[str]:
    return  [student["name"] for student in students]

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
    # TODO Вызовите функцию get_student_names
print(get_student_names(students_list))