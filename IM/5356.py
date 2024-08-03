def vertical(array,N):
    word_list = []
    maxlen = 15
    for j in range(maxlen)):
        for i in range(N):
            try:
                word_list += array[i][j]
            except IndexError:
                continue
    return word_list

T = int(input())
for tc in range(1,T+1):
    N = 5
    for _ in range(T):
        array = [list(map(str, input())) for _ in range(N)]
        break
    result = vertical(array,N)


    print(f'#{tc}', end=' ')
    for text in result:
        print(text, end=' ')






