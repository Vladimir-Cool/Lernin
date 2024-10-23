from random import randint

from data_structure.cyclic_list import CyclicList


def get_random_input():
    n = randint(1, 1000)
    k = randint(0, min(n-1, 100))

    input_str = ''
    for _ in range(n):
        random_int = randint(-10 ** 9, 10 ** 9)
        input_str += f'{random_int} '

    return n, k, input_str

# # n, k = 6, 1
# input_str = '5 -5 5 -5 5 -5'

# n, k = 3, 1
# input_str = '-1 -2 -3'

# n, k = , 100
# input_str = '8'

n, k, input_str = get_random_input()

print(n, k)
print(input_str)

def get_input_data() -> tuple[int, int, str]:
    """ Читает ввод и готовит переменные для работы"""
    n, k = map(int, input().split())
    input_str = input()
    return n, k, input_str

def get_cyclic_list_from_string(input_str: str) -> CyclicList:
    """ Получаем циклический список из строки"""
    cyclic_list = CyclicList()
    cyclic_list.append_list(map(int, input_str.split()))
    return cyclic_list

def get_relevant_selection(n: int, k: int, input_str: str) -> list:
    """ Возвращает наиболее релевантную выборку"""
    max_list = []
    max_sum = -100_000
    cyclic_list = get_cyclic_list_from_string(input_str)

    for index in range(n):
        for i in range(n):
            current_sum = sum(cyclic_list[index:n + index - i])
            # print(cyclic_list[index:n + index - i], current_sum)
            if current_sum > max_sum:
                max_sum = current_sum
                max_list = cyclic_list[index: n + index - i].copy()
            elif current_sum == max_sum:
                if len(cyclic_list[index:n + index - i]) > len(max_list):
                    max_list = cyclic_list[index: n + index - i].copy()

            i -= 1
    return max_list


def filter_state(articles_list: list, k: int):
    for _ in range(k):
        if len(articles_list) < 2:
            break

        if min(articles_list) < 0:
            articles_list.remove(min(articles_list))




articles_list = get_relevant_selection(n, k, input_str)
# print(articles_list)
filter_state(articles_list, k)

print(articles_list, sum(articles_list))
