from re import match, search


answer = (b"answer Fail fail ").decode("utf-8")
pattern = r"[Ff]ail"
result = search(pattern, answer)

if result:
    print("да")
else:
    print("нет")
