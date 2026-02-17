import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k, a, b, x, y = map(int, input().split())
    res = 0
    if x < y:
        if k >= a:
            num_a = (k - a) // x + 1
            res += num_a
            k -= num_a * x
        if k >= b:
            num_b = (k - b) // y + 1
            res += num_b
    else:
        if k >= b:
            num_b = (k - b) // y + 1
            res += num_b
            k -= num_b * y
        if k >= a:
            num_a = (k - a) // x + 1
            res += num_a
    print(res)
