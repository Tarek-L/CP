import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    mini = float("inf")
    win = 1
    cost = 0
    length = len(arr)

    for i in range(1, length):
        if arr[i] == arr[i - 1]:
            win += 1
        else:
            cost = (n - win) * arr[i - 1]
            mini = min(mini, cost)
            win = 1

    cost = (n - win) * arr[i]
    mini = min(mini, cost)
    print(mini)
