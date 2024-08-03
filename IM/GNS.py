def viewCount(array, numbers):
    viewcount = 0
    for number in array:
        if number == numbers:
            viewcount += 1
    return viewcount

def GNS(arr,num):
    N = 10
    counts = [0] * N
    for i in range(N):
        counts[i] = viewCount(arr,num[i])
    return counts

T = int(input())
for tc in range(1, T + 1):
    Except = input()
    arr = list(map(str, input().split()))
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    N = 10
    numCounts = GNS(arr,num)
    total = []
    for i in range(N):
        total += [num[i]] *numCounts[i]
    print(f'#{tc}')
    print(' '.join(total))

