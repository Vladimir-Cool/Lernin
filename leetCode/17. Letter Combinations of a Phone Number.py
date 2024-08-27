from typing import List


def merging_list(list_srt1: List[str], list_str2: List[str]) -> List[str]:
    new_list = []

    for i in range(len(list_srt1)):
        for j in range(len(list_str2)):
            new_list.append(list_srt1[i] + list_str2[j])

    return new_list


def letterCombinations(digits: str) -> List[str]:
    phone_number_button = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    if digits:
        result_list = phone_number_button[digits[0]]

        for i in range(len(digits) - 1):
            result_list = merging_list(result_list, phone_number_button[digits[i + 1]])

        return result_list
    return []


# two = ["a", "b", "c"]
# three = ["d", "e", "f"]
#
# print(merging_list(two, three))

print(letterCombinations(""))
