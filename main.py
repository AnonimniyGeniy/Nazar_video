import time
from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from data_gen import gen_data

# Компаратор для лексикографического сравнения строк
def comparator(a, b):
    return a < b


if __name__ == '__main__':
    # Генерируем данные при необходимости
    # gen_data(10000)

    # Считываем данные из файла
    data = open("data.txt").read().splitlines()

    # Сортируем массивы с помощью трёх алгоритмов
    start = time.time()
    quick_sort(data.copy(), comparator)
    print("Quick sort:", time.time() - start)

    start = time.time()
    merge_sort(data.copy(), comparator)
    print("Merge sort:", time.time() - start)

    start = time.time()
    bubble_sort(data.copy(), comparator)
    print("Bubble sort:", time.time() - start)

    '''
    Output:
    Quick sort: 0.035240888595581055
    Merge sort: 0.029958248138427734
    Bubble sort: 7.7840728759765625
    '''
