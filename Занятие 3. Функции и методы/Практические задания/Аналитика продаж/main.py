def calculate_total_sales(sales_list):
    total = 0
    for sale in sales_list:
        total += sale["quantity"] * sale["price_per_unit"] # TODO Вычислите общую стоимость проданных товаров из списка `sales_list`
    return total


sales_data = [
    {"product": "Футболка", "quantity": 10, "price_per_unit": 500},
    {"product": "Джинсы", "quantity": 5, "price_per_unit": 1000},
    {"product": "Кроссовки", "quantity": 3, "price_per_unit": 1500},
]

total_sales = calculate_total_sales(sales_data) ...  # TODO Вызовете функцию calculate_total_sales и передайте в функцию значение переменной sales_data
print(f"Общая стоимость проданных товаров: {total_sales}")
