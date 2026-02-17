def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                print("YES")
                print(2)
                print(arr[i], arr[j])
                return
    print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
