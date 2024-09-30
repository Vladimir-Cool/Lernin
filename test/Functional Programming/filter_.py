
def is_int(element):
    return isinstance(element, int)

int_list = filter(is_int, [1, "2", 3, [4, 5], 6, "7", "8"])

print(list(int_list))