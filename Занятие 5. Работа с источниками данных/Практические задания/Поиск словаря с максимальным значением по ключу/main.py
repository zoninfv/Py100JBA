import json


FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME, encoding="utf-8") as file:
        json_data = json.load(file)  # TODO считать содержимое JSON файла

        return max(json_data,key=lambda p: p["score"]) # TODO найти максимальный элемент по ключу score


if __name__ == '__main__':
    print(task())


