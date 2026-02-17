import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = False

    for i in range(1, n - 1):
        b = s[i]
        a = s[:i]
        c = s[i + 1 :]
        if b in a + c:
            res = True
            break
    if res:
        print("Yes")
    else:
        print("No")
