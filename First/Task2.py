def input_(msg):
    input_data = input(msg)
    if not input_data.isdigit(): return input_("Вы ввели не число. Введите число: ")
    if 10 <= int(input_data) <= 50: return input_data
    return input_("Ваше число не диапазоне. Введите число:")
print(input_("Введите число: "))