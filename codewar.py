def sum_two_smallest_numbers(numbers):
    temp = int()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                print("im in if")
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

            else:
                print("Im in else")
    print(numbers)
    return(numbers[0] + numbers[1])

k = sum_two_smallest_numbers([25, 42, 12, 18, 22])
print(k)
