from typing import List

""" Это решение находит общую наибольшую подстроку из любого места"""


def match_checking(word1: str, i: int, word2: str, j: int) -> str:
    chek_str = ""
    len_iter = min(len(word1) - i, len(word2) - j)

    for z in range(len_iter):
        if word1[i + z] == word2[j + z]:
            chek_str += word1[i + z]
        else:
            break
    return chek_str


def max_prefix(word1: str, word2: str):
    len_1 = len(word1)
    len_2 = len(word2)

    chek_str = ""

    for i in range(len_1):
        for j in range(len_2):
            if word1[i] == word2[j]:
                new_chek_str = match_checking(word1, i, word2, j)
                chek_str = (
                    new_chek_str if len(new_chek_str) > len(chek_str) else chek_str
                )
            #     print(chek_str)
            # print("___")
    return chek_str


def main(word_list: List[str]):
    chek_str = word_list[0]
    list_len = len(word_list)

    for i in range(list_len - 1):
        if chek_str:
            chek_str = max_prefix(chek_str, word_list[i + 1])
        else:
            return ""

    return chek_str


# result = max_prefix("cart", "wocatcar")
# print(result)
# print(match_checking("cat", 0, "mocatr", 2))

strs = ["reflower", "flow", "flight"]

end = main(strs)
print(end)
