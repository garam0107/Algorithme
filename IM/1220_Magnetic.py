def magnetic(arr):
    stack = []
    count = 0
    N = 5
    for i in range(N):
        for j in range(N):
            if not stack and arr[j][i] == 1:
                stack.append(arr[j][i])
            # elif arr[j][i] == 1 and stack[-1] == 2:
            #     stack.append(arr[j][i])
            # elif arr[j][i] == 2 and stack[-1] == 1:
            #     stack.append(arr[j][i])
    return stack





# T = 10
# for tc in range(1,T+1):
#     N = int(input())
array = [list(input().split()) for _ in range(5)]
answer = magnetic(array)
print(answer)

