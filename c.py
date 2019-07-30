if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    max = arr[0]
    minn = None
    for i in range(1, n+1):
        if arr[i] < max:
            minn = arr[i]
            break

    print(minn)
