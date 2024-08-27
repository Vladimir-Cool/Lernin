

n = int(input())

parents = {}
for _ in range(n):
    a = input().split(" : ")
    parents[a[0]] = [] if len(a) == 1 else a[1].split(" ")

print(parents)
