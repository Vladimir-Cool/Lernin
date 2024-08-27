
A = 1
# print(locals().items())
LIST = [3, -7, 8, -200, 35, 0, -20]

sort_ter = []
sort_ter.append(x for x in LIST if x > 0)

print(sort_ter)

SETTINGS = dict((key,val) for key, val in locals().items() if key.isupper())
print(SETTINGS)



