import sys
import threading

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2

        l = list(map(int, data[idx:idx + n]))
        idx += n

        # Prefix sum of 1s
        ones_prefix = [0] * (n + 1)
        for i in range(n):
            ones_prefix[i + 1] = ones_prefix[i] + l[i]

        res = 0
        i = 0

        while i <= n - k:
            # sum of ones in window [i, i + k)
            ones_in_window = ones_prefix[i + k] - ones_prefix[i]
            if ones_in_window == 0:
                res += 1
                i += k + 1
            else:
                i += 1

        results.append(str(res))

    sys.stdout.write('\n'.join(results) + '\n')

threading.Thread(target=main).start()

