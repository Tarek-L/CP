import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    left = []
    right = []
    togg = True

    while n > 0:
        if togg:
            right.append(n)
        else:
            left.append(n)
        n -= 1
        togg = not togg

    res = left[::-1] + right

    print(" ".join(list(map(str, res))))
