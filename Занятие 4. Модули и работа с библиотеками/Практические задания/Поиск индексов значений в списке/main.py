# TODO написать функцию index
def index(list1: list,value1: any) -> list[int]:
    list_index = [i for i, current_value in enumerate(list1) if current_value == value1]
    if not list_index:
        raise ValueError("Значение не найдено")
    return list_index




if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
