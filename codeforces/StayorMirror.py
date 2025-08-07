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
    m = n // 2
    res = [0]*n 
    k = 0
    for i in range(m,n):
        res[i] = max(l[i],2 * n - l[i])
    for i in range(n,m):
        res[i] = min(l[i],2 * n - l[i])
    for i in range(n-1):
        for j in range(i + 1):
            if res[j] < res[i]:
                k +=1
    print(k)

    

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
