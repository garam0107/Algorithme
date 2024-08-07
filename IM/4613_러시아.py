
def russia(array,N,M):

    min_v = N*M  # N*M의 행을 다 바꾸는 값을 임의로 최솟값으로 설정(이 경우보다 큰 경우는 없기 때문)
    for a in range(1,N-1):
    # a: 첫번째 행부터 a까지 화이트로 색칠할 기준점, a의 최대 기준점은 N-3
        for b in range(a+1,N): # b: a부터 b까지 블루로 색칠할 기준점, b의 최대 기준점은 N-2
            counts = 0  # counts:리스트의 모든 요소를 돌면서 색칠한 횟수를 더하는 변수
            for i in range(a):  # 0부터 a-1행까지 화이트로 칠하는 범위
                for j in range(M):
                    if array[i][j] != 'W': # W가 아닐 경우 칠해야 하므로 counts에 +1
                        counts += 1
            for i in range(a,b):  # a부터 b-1행까지 블루로 칠하는 범위
                for j in range(M):
                    if array[i][j] != 'B': # B가 아닐 경우 칠해야 하므로 counts에 +1
                        counts += 1
            for i in range(b,N):  # b부터 마지막 행까지 레드로 칠하는 범위
                for j in range(M):
                    if array[i][j] != 'R': # R이 아닐 경우 칠해야 하므로 counts에 +1
                        counts += 1
            if min_v > counts:
                min_v = counts

    return min_v

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    array = [list(input()) for _ in range(N)]

    answer = russia(array,N,M)
    print(f'#{tc} {answer}')