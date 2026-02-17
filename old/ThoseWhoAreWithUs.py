import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    max_val = max(max(row) for row in a)

    row_counts = [row.count(max_val) for row in a]
    max_row_count = max(row_counts)
    rows = [i for i, c in enumerate(row_counts) if c == max_row_count]

    col_counts = []
    for j in range(m):
        count = sum(1 for i in range(n) if a[i][j] == max_val)
        col_counts.append(count)
    max_col_count = max(col_counts)
    cols = [j for j, c in enumerate(col_counts) if c == max_col_count]

    overlap_free = False
    for i in rows:
        for j in cols:
            if a[i][j] != max_val:
                overlap_free = True
                break
        if overlap_free:
            break

    if overlap_free:
        print(max_val - 1)
    else:
        print(max_val)
