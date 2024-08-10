def calcul(array):
    stack = []
    answer = []
    for c in array:
        if c.isdigit():
            answer.append(c)
        elif c == '+':
            if not stack:
                stack.append(c)
            elif stack[-1] == '+':
                answer.append(stack.pop())
                stack.append(c)
            elif stack[-1] == '*':
                while stack:
                    answer.append(stack.pop())
                stack.append(c)
        elif c == '*':
            if not stack:
                stack.append(c)
            elif stack[-1] == '+':
                stack.append(c)
            elif stack[-1] == '*':
                answer.append(stack.pop())
                stack.append(c)
    while stack:
        answer.append(stack.pop())
    return ''.join(answer)

def result_num(array):
    stack = []
    for c in array:
        if c.isdigit():
            stack.append(int(c))
        elif c == '+':
            x1 = stack.pop()
            y1 = stack.pop()
            stack.append(x1+y1)
        elif c == '*':
            x2 = stack.pop()
            y2 = stack.pop()
            stack.append(x2*y2)
    return ''.join(map(str, stack))

T= 10
for tc in range(1,T+1):
    N = int(input())
    array = input()
    express = calcul(array)
    result = result_num(express)
    print(f'#{tc} {result}')