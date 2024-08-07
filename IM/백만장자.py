def money(array, N):
    total = 0
    for i in range(N):
        money_list = []
        for j in range(i+1, N):
            if array[i] < array[j]:
                money_list += [array[j]]
        if money_list:
            total += max(money_list) - array[i]


    return total

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = list(map(int ,input().split()))
    answer = money(array,N)
    print(f'#{tc} {answer}')
