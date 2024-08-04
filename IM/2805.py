def farm(arr, N):
    row = 0        # 시작 위치의 행 번호 0에서부터 아래로 내려가기 위해서 0으로 할당
    col = N // 2   # 시작 위치의 열 번호는 N의 중간값으로 고정
    r = 1
    total = 0     # 탐색을 하면서 총합을 저장할 변수
    dc = [-1,1]   # 현재 위치에서 좌,우 방향을 탐색하기 위한 델타

    while row < N:              # 마지막 행에 도달하면 반복문이 끝남
        total += arr[row][col]  # 현재 위치의 값을 total에 추가
        row = row + r           # 아래 행으로 이동하기 위해 +1

        """
        현재 위치를 첫번째 행에 중앙으로 잡고 시작했기 때문에 행의 위치만 달라지고 열의 위치는 고정입니다.
        그렇기 때문에 행이 열보다 큰 경우, 행과 열이 같은 경우, 행과 열이 작은 경우 세가지가 나옵니다.
        경우마다 좌,우 방향으로 탐색하는 칸 수가 다르기 때문에 if문으로 각 경우마다 이동할 칸의 수를 지정해줬습니다.
        
        """

        if row < col:    # 행의 위치가 열의 위치 보다 작은 경우
            for add in range(1,row+1):  # 현재 위치에서 행의 위치까지 좌우로 탐색하기 위한 변수 add
                for k in range(2):  # 좌우 두 방향만 탐색하기 때문에 범위는 2
                    nc = col + dc[k]*add    # 좌우만 탐색하기 때문에 행의 위치는 그대로 고정
                    total += arr[row][nc]

        if row == col:  # 행의 위치가 열의 위치와 같은 경우, 행과 열의 위치가 같으면 현재 위치는 정중앙
            for add_2 in range(1,(N//2+1)): # 첫번째 열부터 마지막 열까지 탐색
                for k in range(2):
                    nc_2 = col + dc[k] * add_2
                    total += arr[row][nc_2]

        if row > col:    # 행의 위치가 열의 위치보다 큰 경우, 중앙에서 하단으로 내려감
            for add_3 in range(1,N-row):   # N-row는 남은 행의 수를 계산하기 위함
                for k in range(2):
                    nc_3 = col + dc[k] * add_3
                    total += arr[row][nc_3]

    return total



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input())) for _ in range(N)]

    answer = farm(array,N)

    print(f'#{tc} {answer}')
