import sys
from collections import deque

input = sys.stdin.readline


def tile(n: int, box: list[int]):
    return n <= box[0] and n <= box[1] and n <= box[2]


def fits(l: list[int], box: list[int]):
    queue = deque()
    queue.append(box)
    for i in l:
        placed = False
        for _ in range(len(queue)):
            b = queue.popleft()
            if tile(i, b):
                queue.append([i, i, b[2] - i])  
                queue.append([b[0] - i, b[1], b[2]]) 
                queue.append([b[0], b[1] - i, b[2]])
                placed = True
                break
            else:
                queue.append(b) 
        if not placed:
            return False
    return True


def fib(n):
    fib = [1, 2]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[::-1]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    fibl = fib(n)
    res = []
    for _ in range(m):
        box = list(map(int, input().split()))
        res.append("1" if fits(fibl, box) else "0")
    print("".join(res))
