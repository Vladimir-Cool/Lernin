import textwrap

text = "Это длинная строка текста, которую нужно разбить на несколько строк для улучшения читаемости."

# Разбить текст на строки шириной 30 символов
wrapped_text = textwrap.wrap(text, width=30)

# Вывести результат
for line in wrapped_text:
    print(line)