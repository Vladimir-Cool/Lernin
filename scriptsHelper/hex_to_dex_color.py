def hex_to_decimal(hex_number):
    try:
        return int(hex_number, 16)
    except ValueError:
        return "Ошибка: недопустимое 16-ричное число"


# Пример использования
hex_number = "00CED1"  # 16-ричное число
decimal_number = hex_to_decimal(hex_number)
print(decimal_number)
