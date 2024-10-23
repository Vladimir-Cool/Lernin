from random import randint, randrange


n = randint(1, 100_000)
k = randint(0, 100)

result_str = ''
for _ in range(n):
    random_int = randint(-10**9, 10**9)
    result_str += f'{random_int} '

print(result_str)
