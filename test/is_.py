

print(2 == 2)
print(2 is 2)

print('________________________')
# print([1, 2] == [1, 2])
# print([1, 2] is [1, 2])

a = [1, 2]
b = [1, 2]

print(id(a))  # 2696458588544
print(id(b))  # 2696458588544

print(a == b)  # True
print(a is b)  # False

print(True == True or False == False)

