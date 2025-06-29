import sys

input = sys.stdin.readline

t = int(input())


def possible(a, b, right, left, up, down):
    s1 = right[0] - (left[0] + a)
    s2 = up[1] - (down[1] + b)

    if s1 == 0:
        return True
    if s2 == 0:
        return True
    if s1 > 0 and s2 > 0:
        if s2 % b == 0 or s1 % a == 0:
            return True
        else:
            return False
    if s1 < 0:
        if s2 % b == 0:
            return True
    if s2 < 0:
        if s1 % a == 0:
            return True

    return False


for _ in range(t):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    sheet1 = [x1, y1]
    sheet2 = [x2, y2]
    right = sheet1 if x1 > x2 else sheet2
    left = sheet1 if x1 <= x2 else sheet2
    up = sheet1 if y1 > y2 else sheet2
    down = sheet1 if y1 <= y2 else sheet2

    if possible(a, b, right, left, up, down):
        print("YES")
    else:
        print("NO")
