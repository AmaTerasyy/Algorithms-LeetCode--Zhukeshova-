# -*- coding: utf-8 -*-
import random
import sys
import io

# Для корректного вывода русского текста в Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# -------- Функция разбиения массива (Lomuto) --------
def partition(arr, low, high):
    """
    Разбивает массив на две части относительно опорного элемента (pivot).
    Элементы <= pivot перемещаются влево, остальные — вправо.
    Возвращает индекс, на котором оказался pivot.
    """
    pivot = arr[high]  # Опорный элемент — берем последний элемент подмассива
    i = low - 1        # Индекс для элементов <= pivot

    # Проходим по всем элементам кроме pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами

    # Ставим pivot на его правильное место
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Индекс pivot

# -------- QuickSort с рандомизацией --------
def quick_sort(arr, low, high):
    """
    Быстрая сортировка массива на месте (in-place) с использованием
    рандомного выбора опорного элемента.
    """
    if low < high:
        # Выбираем случайный индекс pivot
        pivot_index = random.randint(low, high)
        # Меняем выбранный pivot с последним элементом для схемы Lomuto
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Разделяем массив и получаем индекс pivot
        pi = partition(arr, low, high)

        # Рекурсивно сортируем левую часть массива
        quick_sort(arr, low, pi - 1)
        # Рекурсивно сортируем правую часть массива
        quick_sort(arr, pi + 1, high)

# -------- Пример использования с разными массивами --------
if __name__ == "__main__":
    # Список массивов для тестирования
    test_arrays = [
        [8, 3, 1, 7, 0, 10, 2],
        [5, 9, 1, 4, 7, 3, 6, 2, 8],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]

    # Проходим по каждому массиву
    for idx, arr in enumerate(test_arrays, 1):
        print(f"--- Вариант {idx} ---")
        print("Исходный массив:", arr)
        quick_sort(arr, 0, len(arr)-1)
        print("Отсортированный массив:", arr, "\n")