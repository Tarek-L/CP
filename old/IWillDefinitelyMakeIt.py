import sys
import threading

def solve():
    n, k = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))

    k_val = l[k - 1]
    h = sorted(set(l))  # sorted unique values
    j = 0

    # Binary search to find index of k_val in h
    lo, hi = 0, len(h) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if h[mid] < k_val:
            lo = mid + 1
        elif h[mid] > k_val:
            hi = mid - 1
        else:
            j = mid
            break

    tmp = 0
    while j < len(h) - 1:
        tmp += h[j + 1] - h[j]
        if tmp > h[j]:
            print("NO")
            return
        j += 1

    print("YES")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

threading.Thread(target=main).start()

