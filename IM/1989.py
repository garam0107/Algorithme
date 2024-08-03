T = int(input())
for tc in range(1,T+1):
    arr = list(input())
    reverse_text = arr[::-1]
    answer = 0
    if arr == reverse_text:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')
