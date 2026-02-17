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
    res = []

    pref = [0]*n
    pref[0] = l[0]
    for i in range(1, n):
        pref[i] = min(pref[i-1], l[i])
    suff = [0]*n
    suff[-1] = l[-1]
    for i in range(n-2, -1, -1):
        suff[i] = max(suff[i+1], l[i])

    for i in range(n):
        if l[i] == suff[i] or l[i] == pref[i]:
            res.append("1")
        else:
            res.append("0")
    print(''.join(res))




def main():
    t = inp()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
