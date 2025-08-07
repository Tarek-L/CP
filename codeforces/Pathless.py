import sys
import threading
   
input = sys.stdin.readline
     
def inp(): return int(input())
def inlt(): return list(map(int, input().split()))
def insr(): return list(input().strip())
def invr(): return map(int, input().split())
 
def solve():
    n, s = invr()
    l = inlt()
    su = sum(l)
    alpha = s - su
    if su > s:
        print(*l)
    elif su == s:
        print(-1)
    else:
        if alpha == 1:
            z = l.count(0)
            w = l.count(2)
            o = l.count(1)
            sol = [0]*z + [2]*w + [1]*o
            print(*sol)
        else:
            print("-1")
  
 
    
 
 
 
def main():
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    threading.Thread(target=main).start()
