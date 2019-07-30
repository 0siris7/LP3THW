def swap_case(s):
    a = list(s)
    b = []
    for i in a:
        if i.isupper():
            b.append(i.lower())
        elif i.islower():
            b.append(i.upper())

    return(''.join(b))

if __name__ == '__main__':
    s = input("Enter the string: ")
    result = swap_case(s)
    print(f"The result: {result}")
