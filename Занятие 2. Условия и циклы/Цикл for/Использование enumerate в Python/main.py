for tuple_ in enumerate(["а", "б", "в"]):  # перебираем кортежи с индексом и значением
    print(tuple_)

for pos, value in enumerate("абв", start=13):  # start по умолчанию равен 0, но можно задать произвольное целое число
    print("Позиция:", pos, "->", "Значение:", value)
