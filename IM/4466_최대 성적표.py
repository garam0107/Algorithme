def mySort(score,N):
    for i in range(N):
        for j in range(0,N-i-1):
            if score[j] < score[j+1]:
                score[j],score[j+1] = score[j+1],score[j]
    return score
def maxScore(score,K):
    score = mySort(score,N)
    maxScore = 0
    for i in range(K):
        maxScore += score[i]
    return maxScore

T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    score = list(map(int, input().split()))
    answer = maxScore(score,K)
    print(f'#{tc} {answer}')
