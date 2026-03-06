# -*- coding: utf-8 -*-
import random
import sys
import io

# Для корректного вывода русского текста в Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# -------- Функция разбиения массива (Lomuto) --------
def partition(arr, low, high):
    """
    Разбивает массив на две части относительно pivot:
    элементы <= pivot слева, элементы > pivot справа.
    Возвращает индекс pivot после разбиения.
    """
    pivot = arr[high]  # Опорный элемент
    i = low - 1        # Индекс для элементов <= pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Меняем элементы местами

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Ставим pivot на место
    return i + 1  # Возвращаем индекс pivot

# -------- QuickSelect с рандомизацией --------
def quick_select(arr, k):
    """
    Возвращает k-й наименьший элемент в массиве (k начинается с 0)
    без полной сортировки массива.
    """
    low = 0
    high = len(arr) - 1

    while True:
        if low == high:  # Если остался один элемент
            return arr[low]

        # Рандомный выбор pivot
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Разделяем массив
        pi = partition(arr, low, high)

        # Проверяем, где находится k
        if k == pi:
            return arr[pi]          # k-й элемент найден
        elif k < pi:
            high = pi - 1           # Ищем в левой части
        else:
            low = pi + 1            # Ищем в правой части

# -------- Примеры использования с разными массивами и k --------
if __name__ == "__main__":
    test_cases = [
        ([9, 4, 7, 1, 3, 6, 2, 8, 5], 4),   # 5-й по величине элемент
        ([5, 9, 1, 4, 7, 3, 6, 2, 8], 0),   # минимальный элемент
        ([10, 20, 30, 40, 50, 60], 3),      # средний элемент
        ([7, 2, 9, 4, 1, 5, 3, 8, 6], 8)    # максимальный элемент
    ]

    for idx, (arr, k) in enumerate(test_cases, 1):
        print(f"--- Вариант {idx} ---")
        print("Массив:", arr)
        print(f"k = {k}")
        result = quick_select(arr.copy(), k)
        print(f"{k}-й наименьший элемент:", result, "\n")