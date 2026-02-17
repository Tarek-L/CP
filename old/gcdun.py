import sys
import threading
from math import gcd

def check_possible(p, s):
    n = len(p)
    a = [gcd(p[i], s[i]) for i in range(n)]  

    pref = [0] * n
    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = gcd(pref[i-1], a[i])

    suff = [0] * n
    suff[-1] = a[-1]
    for i in range(n-2, -1, -1):
        suff[i] = gcd(suff[i+1], a[i])

    return "YES" if (pref == p and suff == s) else "NO"

def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    s = list(map(int, sys.stdin.readline().split()))
    print(check_possible(p, s))

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

threading.Thread(target=main).start()

