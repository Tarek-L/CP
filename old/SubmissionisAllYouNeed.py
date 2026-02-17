import sys
import threading

input = sys.stdin.readline

def inp(): return int(input())
def inlt(): return list(map(int, input().split()))
def insr(): return list(input().strip())
def invr(): return map(int, input().split())

def solve():
    n = inp()
    l = inlt()
    print(sum(l) + l.count(0))

def main():
    t = inp()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
