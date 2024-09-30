result = map(lambda x: x**2, [1, 2, 3, 4, 5])

print(list(result))


def removes_spaces(string: str):
    return string.replace(" ", "")

list_word = [
    "Слова написанный через пробел",
    "Как ваши дела?",
    "Привет мир, я пришел"
]

result_list = map(removes_spaces, list_word)

print(list(result_list))