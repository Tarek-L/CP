import sys
import threading

input = sys.stdin.readline

def inp(): return int(input())
def inlt(): return list(map(int, input().split()))
def insr(): return list(input().strip())
def invr(): return map(int, input().split())

def solve():
    n , m = invr()
    l = inlt()
    l.sort()
    res = 0
    i = n-1
    while m > 0 and i >=0:
        res += l[i]*m
        i -= 1
        m -= 1
    print(res)





def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
