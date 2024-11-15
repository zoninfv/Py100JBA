# TODO Напишите функцию decimal_to_hex
def decimal_to_hex() -> dict[int, str]:
    return {decimal: hex(decimal) for decimal in range(16)}
if __name__ == '__main__':
    converted_dict = decimal_to_hex()
    print(converted_dict)  # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами
