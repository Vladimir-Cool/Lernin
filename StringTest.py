from re import match, search


answer = (b"answer Fail fail ").decode("utf-8")
pattern = r"[Ff]ail"
result = search(pattern, answer)

if result:
    print("да")
else:
    print("нет")

list_test = ["1", "2", "3"]
string_test = "Строка для теста"

print(string_test.split(" "))
print(" ".join(list_test))

