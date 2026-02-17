import sys
import threading

input = sys.stdin.readline

def solve():

    n = int(input())
    res = 0

    a_list = []
    b_list = []
    c_list = []
    d_list = []
    
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
        d_list.append(d)   

def main():
    t = int(input())
    for _ in range(t):
        solve()

threading.Thread(target=main).start()
