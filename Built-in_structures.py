# Built-in_structures - встроенные структуры данных в ЯП Python.
# Этот файл будет как краткое повторение для себя.

# В языке программирования Python всего 4 встроенных структуры данных. 
# Это 
    # список (list ), 
    # кортеж (tuple), 
    # словарь (dictionary ) и набор или 
    # множество(set). 
# Каждый из них по-своему уникален.

# ===========================================================================================
                                        # Список|Кортеж
# Структура данных, в которой хранится набор элементов в Python, называется списком. 
# Другими словами, список содержит последовательность элементов.
# Отмечу, что список в Python - это изменяймый тип данных с неопределенной длиной и способный
# хранить элементы разных типов. Кортеж - не изменяймый тип данных!
# В Python представлен по умолчанию такие типы/структуры данных.
# Если же нужен именно статический массив, способный хранить разные типы данных в
# своей последовательности - то можно использовать другой тип данных втроенный в ЯП - кортеж.
# Если же нужен статический/динамический массив, способный хранить элементы
# только одного типа данных - то реализация будет за программистом.

# Далее можно еще долго говорить о всяких ньюансах этих типов данных, и что они 
# по разному занимают место, и то, что можно всеже найти способ изменить кортеж, как их 
# создавать и так далее. Кстати, про создание, для меня, если это возможно, для создания(и наполнение)
# списка использовать списковое включение является более предпочтительным способом.


from typing import List
from timeit import timeit

def filling_the_list_by_adding_method(number_of_elements: int) -> List[int]:
    list_of_values = []
    
    for i in range(number_of_elements):
        list_of_values.append(i)
    
    return list_of_values


def filling_list_with_list_inclusion(number_of_elements: int) -> List[int]:
    return [
        i for i in range(number_of_elements)
    ]



if __name__ == "__main__":
    number_of_elements = 100000

    adding_method = timeit(
        "filling_the_list_by_adding_method(number_of_elements)", 
        setup="from __main__ import filling_the_list_by_adding_method, number_of_elements", 
        number=1
    )

    list_inclusion = timeit(
        "filling_list_with_list_inclusion(number_of_elements)", 
        setup="from __main__ import filling_list_with_list_inclusion, number_of_elements", 
        number=1
    )
    print('Результаты замера времени при разных способах наполнения списков:')
    print(f'adding_method --->>> {adding_method:.5f}')
    print(f'list_inclusion --->>> {list_inclusion:.5f}')

# далее повторю методы списка/кортежа
