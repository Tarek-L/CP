t = int(input())
for q in range(t):
    x = int(input())

    arr = [0, 0, 0]
    count = 0

    while min(arr) < x:
        i = arr.index(min(arr))
        j = arr.index(min(arr[(i + 1) % 3], arr[i - 1]))
        if arr[j] == 0:
            arr[i] = 1
        elif 2 * arr[j] > x:
            arr[i] = x
        else:
            arr[i] = 2 * arr[j] + 1
        count += 1

    print(count)
