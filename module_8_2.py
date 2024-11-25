# Сложные моменты и исключения в стеке вызовов функции

def personal_sum(numbers):
    """
    Подсчитывает сумму чисел в коллекции и количество некорректных данных.

    Args:
    numbers: Коллекция чисел.

    Returns:
    tuple: Кортеж из двух значений: сумма чисел и количество некорректных данных.
    """
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    """
    Подсчитывает среднее арифметическое чисел в коллекции.

    Args:
    numbers: Коллекция чисел.

    Returns:
    float: Среднее арифметическое чисел или None, если передан некорректный тип данных.
    """
    try:
        if not isinstance(numbers, (list, tuple, set)):
            print('В numbers записан некорректный тип данных')
            return None
        total, incorrect = personal_sum(numbers)
        if len([num for num in numbers if isinstance(num, (int, float))]) == 0:
            return 0
        average = total / len([num for num in numbers if isinstance(num, (int, float))])
        return average
    except Exception as e:
        print(f'Произошла ошибка: {e}')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')