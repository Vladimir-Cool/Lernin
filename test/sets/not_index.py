
new_set = {1, 2, 3, 4, 5}
try:
    new_set[0]
except TypeError as e:
    print('Ошибка', e)
    