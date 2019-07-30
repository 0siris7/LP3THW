a = [1, 2, 3 ,42 ,51,12,76,22]

max = a[0]

for i in range(0, len(a)):
    for j in range(1, len(a)):
        if a[j] > a[i]:
            max = a[j]

print(max)
