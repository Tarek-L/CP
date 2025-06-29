import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    classroom = list(map(int, input().split()))
    classroom.sort()

    start = deque(classroom)
    end = deque(classroom)

    res = []

    def bestCouple(start: deque, end: deque) -> list[int]:
        candidates = [
            (start[0], end[-1]),
            (start[-1], end[0]),
        ]
        pair = max(candidates, key=lambda p: abs(p[0] - p[1]))

        if pair == (start[0], end[-1]):
            start.popleft()
            end.pop()
        else:
            start.pop()
            end.popleft()

        return list(pair)

    for _ in range(n):
        res.append(bestCouple(start, end))

    for pair in res:
        s = " ".join(map(str, pair))
        print(" ".join([s] * 3))
