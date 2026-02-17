import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b,x,y = map(int,input().split())
    diff = b - a
    res = 0
    if diff >= 0:
        if y >= x :
            print(diff * x)
        else:
            while b - a > 0:
                if a ^ 1 == a + 1:
                    res += y
                else:
                    res += x
                a += 1
            print(res)
    else:
        if (a ^ 1) - b == 0 :
            print(y)
        else:
            print("-1")

