a = []
x = int(input("enter stuff:"))
for i in range(x):
    name = input()
    score = float(input())
    a.append([name, score])

print(f"Unsorted: {a}")
a.sort(key = lambda x: x[1])
print(f"Sorted {a}")
minn = a[1][1]
print(minn)
name = a[1][0]
print(name)
print('-' * 10)
for i in range(2, len(a)):
    if a[i][1] <= minn:
        name += '\n' + a[i][0]

k = name.split('\n')


for i in sorted(k):
    print(i)
