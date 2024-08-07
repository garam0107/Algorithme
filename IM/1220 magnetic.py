def magnetic(array,N):
    stack = []
    for i in range(N):
        for j in range(N):
            if array[j][i] == 0: continue
            if array[j][i] == 1 and array[j][i] not in stack:
                stack.append(array[j][i])

            if array[j][i] == 2 and array[j][i] not in stack:
                stack.append(array[j][i])

            if array[j][i] == 1 and stack[-1] != 1:
                stack.append(array[j][i])

            if array[j][i] == 2 and stack[-1] != 2:
                stack.append(array[j][i])
        if stack[0] == 2:
            stack.pop(0)
        if stack[-1] == 1:
            stack.pop()

    return len(stack) // 2


import sys
sys.stdin = open('input (2).txt', 'r')


T = 10
for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    answer = magnetic(array,N)

    print(f'#{tc} {answer}')