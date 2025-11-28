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
    if len(set(l)) < len(l):
        print("YES")
    else:
        print("NO")
    


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
