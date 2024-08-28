def func(dct):
    for key in dct.keys():
        dct[key] += 2


dct = {
    'a': 1,
    'b': 2,
    'c': 3,
}

func(dct)
print(dct)