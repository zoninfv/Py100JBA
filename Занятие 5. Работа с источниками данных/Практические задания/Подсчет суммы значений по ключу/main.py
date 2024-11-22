import json


FILENAME = "input.json"


def task() -> int:
    with open (FILENAME, encoding="utf-8") as file:
        json_data = json.load(file)

    list1 = [item["contains_improvement_appeals"] for item in json_data]
    return sum(list1)


if __name__ == '__main__':
    print(task())




# Запись данных в файл в формате JSON
#with open(filename, 'w', encoding="utf-8") as file:
    #json.dump(data, file, indent=indent, ensure_ascii=ensure_ascii)

# Сериализация данных в строку JSON
#json_data = json.dumps(data, indent=indent, ensure_ascii=ensure_ascii)
#print("Сериализация данных с помощью метода `dumps`:", json_data)

# Чтение данных из файла в формате JSON
#with open(filename, encoding="utf-8") as file:
    #data = json.load(file)
#print("Десериализованные данные из JSON файла в python объект:", data)

# Десериализация данных из строки JSON
#data = json.loads(json_data)
#print("Десериализованные данные из JSON строки в python объект:", data)