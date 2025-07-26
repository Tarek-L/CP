import sys
import threading

def solve():

    n, k = map(int,input().split())
    l, r, real = [], [], []
    maxi = []

    for _ in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        l.append(a)
        r.append(b)
        real.append(c)
    exists = any(x > k for x in real)

    if not 




def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        solve()

threading.Thread(target=main).start()
