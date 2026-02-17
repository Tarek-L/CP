import sys
import threading

input = sys.stdin.readline

def solve():
    n, m = map(int,input().split())
    if n == 1  or m == 1 :
        print("NO")
    elif n == 2 or m == 2:
        if n >= 3 or m >= 3:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")


def main():
    t = int(input())
    for _ in range(t):
        solve()

threading.Thread(target=main).start()
