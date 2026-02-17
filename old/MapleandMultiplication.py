import sys
import threading

input = sys.stdin.readline

def inp(): return int(input())
def inlt(): return list(map(int, input().split()))
def insr(): return list(input().strip())
def invr(): return map(int, input().split())

def solve():
    a ,b = invr()
    if a == b:
        print("0")
        return
    if a % b == 0 or b % a == 0:
        print("1")
        return
    print("2")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()
