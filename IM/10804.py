T = int(input())
for tc in range(1,T+1):
    array = list(input())
    answer = []
    mirror_text = array[::-1]
    for i in mirror_text:
        if i == 'b':
            answer += 'd'
        if i == 'd':
            answer += 'b'
        if i == 'q':
            answer += 'p'
        if i == 'p':
            answer += 'q'
    print(f'#{tc} {"".join(answer)}')




