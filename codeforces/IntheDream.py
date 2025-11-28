import sys
import threading

input = sys.stdin.readline

def inp(): return int(input())
def inlt(): return list(map(int, input().split()))
def insr(): return list(input().strip())
def invr(): return map(int, input().split())

def solve():
    a ,b ,c ,d = invr()
    tmp1 = max(a, b)
    tmp2 = 2 * min(a ,b) + 2
    c -= a
    d -= b
    fh =  False
    if tmp1 <= tmp2:
        fh = True
    else:
        print("NO")
        return

    tmp1 = max(c, d)
    tmp2 = 2 * min(c ,d) + 2

    if tmp1 <= tmp2 and fh:
        print("YES")
    else:
        print("NO")
        return
    

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
