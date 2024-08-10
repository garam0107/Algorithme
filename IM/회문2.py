def mysort(array):
    return array[::-1]
T = 10
for _ in range(T):
    N = 100
    tc = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    max_value = 0

    # 행 탐색
    for i in range(N):
        for k in range(N):
            new_list = []
            text_len = 0
            for add in range(k, N):
                new_list += arr[i][add]
                if new_list == mysort(new_list):
                    text_len = len(new_list)
                if max_value < text_len:
                    max_value = text_len

    # 열 탐색
    row = 0
    for idx in range(N):
        for k in range(N):
            new_list2 = []
            text_len2 = 0
            for add2 in range(k, N):
                new_list2 += arr[add2][idx]
                if new_list2 == mysort(new_list2):
                    text_len2 = len(new_list2)
                if max_value < text_len2:
                    max_value = text_len2

    print(f'#{tc} {max_value}')


