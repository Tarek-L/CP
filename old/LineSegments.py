
import sys
import math

input = lambda: sys.stdin.readline().strip()

t = int(input())

def possible(px, py, qx, qy, l, n):
    dist = math.sqrt((px - qx) ** 2 + (py - qy) ** 2)
    l.sort(reverse=True) 
    
    if dist == 0:
        if n == 2:
            return abs(l[0] - l[1]) < 1e-8
        elif n == 1:
            return False
        elif sum(l) - l[0] >= l[0]:
            return True
        else:
            return False
    elif sum(l) >= dist and n > 1:
        if l[0] - dist > sum(l) - l[0] + 1e-8:
            return False
        else:
            return True
    elif n == 1 and abs(l[0] - dist) < 1e-8:
        return True
    else:
        return False

for _ in range(t):
    n = int(input())
    px, py, qx, qy = map(int, input().split())
    l = list(map(int, input().split()))
    if possible(px, py, qx, qy, l, n):
        print("Yes")
    else:
        print("No")
