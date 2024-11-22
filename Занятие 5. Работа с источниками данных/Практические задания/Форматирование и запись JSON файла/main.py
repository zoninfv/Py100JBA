import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
    with open (INPUT_FILE, encoding="utf-8") as file:
        json.data = json.load(file)

    with open (OUTPUT_FILE,"w", encoding="utf-8") as file:
        json.dump(json.data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки задания
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")


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