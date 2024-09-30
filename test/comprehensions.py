
test_set = (value**2 for value in range(100) if value % 2 == 0)
print(test_set)


for i in test_set:
    print(type(i))
    print(i)

