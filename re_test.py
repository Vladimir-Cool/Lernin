import re


def re_search(text: str, search_str: str) -> bool:
    """Поиск подстроки в строке"""
    if re.search(search_str, text, re.IGNORECASE):
        return True
    return False


def re_search_list(text: str, search_list: list) -> bool:
    """Поиск первого совпадения слова из списка с текстом"""
    for search_str in search_list:
        if re.search(search_str, text, re.IGNORECASE):
            return True
    return False


# print(re_search("Прикольно получилось", "пи"))

print(re_search_list("Прикольно получилось", ["пу", "прик", "пав"]))
