import sys
import threading

def solve():
    x = int(input())
    res = float('inf')
    while x > 0:
        res = min(res,(x % 10))
        x //= 10
    
    print(int(res))


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        solve()

threading.Thread(target=main).start()
