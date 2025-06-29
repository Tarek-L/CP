import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    doors = input().split()
    for i in range(n):
        if doors[i] == "1":
            break
    for j in range(n):
        if doors[n - 1 - j] == "1":
            break

    if len(doors) - i - j > x:
        print("NO")
    else:
        print("YES")
