json_data = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

json_str = '{"name": "John", "age": 25, "city": "New York"}'  # Так будет выглядеть словарь json_data в виде JSON строки
# Сериализация данных в формате JSON
with open('output.json', 'w', encoding="utf-8") as f:
    f.write(json_str + '\n')


csv_data = [
    ['John', '25', 'New York'],
    ['Alice', '30', 'London'],
    ['Bob', '35', 'Paris']
]

# Сериализация данных в формат CSV
with open('output.csv', 'w', encoding="utf-8") as f:
    lines = [",".join(d) for d in csv_data]
    for line in lines:
        f.write(line + '\n')
