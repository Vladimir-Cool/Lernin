def set_child(parent, buffer):
    if not parent in dict_child.keys():
        dict_child[parent] = set()

    for key in base.keys():
        if buffer in base[key]:
            dict_child[parent].add(key)
            set_child(parent, key)


base = dict()
dict_child = {}


n = int(input())
while n:
    line = input()
    if line.find(":") > 0:
        cls1 = line.split(" : ")
        base[cls1[0]] = set(cls1[1].split(" "))
    else:
        base[line] = {}
    n -= 1

# for i in base:
#     print(i, base[i])

for key in base.keys():
    set_child(key, key)

# for i in dict_child:
#     print(i, dict_child[i])

k = int(input())
while k:
    line = input().split(" ")
    class1 = line[0]
    class2 = line[1]
    if class1 == class2:
        print("Yes")
    else:
        if class2 in dict_child[class1]:
            print("Yes")
        else:
            print("No")
    k -= 1
