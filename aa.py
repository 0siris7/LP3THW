a = open('cookie1.txt')
print(a.read())
a.seek(0)
k = a.readlines()
for w in k:
    print(w.strip())
