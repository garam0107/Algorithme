def balloon(arr,N,M):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    shot = 4
    maxValue = 0
    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            for k in range(shot):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    total += arr[nr][nc]
            if maxValue < total:
                maxValue = total
    return maxValue


T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxShot = balloon(arr,N,M)
    print(f'#{tc} {maxShot}')



