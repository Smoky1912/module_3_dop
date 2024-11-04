def calculate_structure_sum(data):  # зададим функцию
    total_sum = 0  # зададим начальную сумму нулём

    def recursive_sum(element):  # зададим влож. ф-ю
        nonlocal total_sum      # запрос переменной из внеш. функции
        if isinstance(element, int):   # является ли element целым числом
            total_sum += element    # добавим элемент к общ. сум.
        elif isinstance(element, str):  # является ли element строкой
            total_sum += len(element)  # добавим длину строки к общ. сум.
        elif isinstance(element, (list, tuple, set)):  # элемент: список, кортеж или множество
            for sub_element in element:  # цикл чтобы перебрать каждый элементы внутри element
                recursive_sum(sub_element) # рекурсивно обрабатываем каждый получ. эл из списка, кортежа или множества
        elif isinstance(element, dict): # является ли element словарём
            for key, value in element.items(): # цикл чтобы перебрать каждый ключ и значение
                recursive_sum(key)   # рекурсивно обрабатаем ключи
                recursive_sum(value) # рекурсивно обрабатаем значения
    recursive_sum(data) # рекрурсия для обхода всей структуры заданных данных
    return total_sum # вернем итоговую сумму

# Пример
data_structure = [
    [14, 3.14, 3],  # список
    {'Алэр': 8, 'Рэла': 4},  # словарь
    (13, {'Алэр': 8, 'Рэла': 4}),   # кортеж со вложенным словарём
    "Следите за монстрами, которых Вы создаете",  # строка
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # кортеж с разными типами данных
# () - пустой кортеж
# [{(4, 'Апрель', ('Ноябрь', 11))}] - список
# {(4, 'Апрель', ('Ноябрь', 11))} - множество
# (4, 'Апрель', ('Ноябрь', 11)) - кортеж
# 4 - число, 'Апрель' - строка, ('Ноябрь', 11) - кортеж
]

result = calculate_structure_sum(data_structure)
print(result)
