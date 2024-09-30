from functools import reduce


result_reduce = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5, 6,])

print(result_reduce)
