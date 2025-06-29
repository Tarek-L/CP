import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    l = list(map(int, input().split()))

    a = abs(s - l[0])
    b = abs(s - l[-1])

    if l[-1] <= s:
        print(a)
    elif l[0] >= s:
        print(b)
    else:
        print(a + b + min(a, b))
