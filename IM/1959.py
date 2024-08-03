# def myLen(lst):
#     mylen = 0
#     for _ in lst:
#         mylen += 1
#     return mylen
T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2)]
    maxValue = 0
    if N < M:
        for i in range(M-N+1):
            total = 0
            for j in range(N):
                total += arr[0][j] * arr[1][i+j]
            if maxValue < total:
                maxValue = total
    if N > M:
        for i in range(N-M+1):
            total = 0
            for j in range(M):
                total += arr[1][j] * arr[0][i+j]
            if maxValue < total:
                maxValue = total
    print(maxValue)


