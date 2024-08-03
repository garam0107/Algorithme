"""
당근 크기의 리스트가 주어지고 연속으로 커지는 당근의 갯수는
최대 얼마인지 확인, 연속으로 커지지 않는 최소 길이는 1
당근의 크기는 1~10까지의 정수
ex ) 1 2 3 1 2 = 3  ,  1 3 5 6 8 1 2 = 2
"""

def myLen(c):   # 리스트의 길이를 세는 함수
    mylen = 0
    for _ in c:
        mylen += 1
    return mylen
T = int(input())
for tc in range(1,T+1):
    N = int(input())   # 당근의 개수를 입력받음
    carrot = list(map(int, input().split()))  # 당근의 크기를 개수만큼 입력받아서 리스트로 저장
    counts = 0   # 연속된 당근의 개수를 세는 변수
    maxValue = 0 # 연속된 당근의 개수 중 최대를 구하기 위한 변수
    for i in range(myLen(carrot)-1): # 리스트의 개수에서 1을 빼는 이유는 N-1번째 요소와 N번째 요소를 마지막으로 비교할 것이기 때문
        if carrot[i] < carrot[i+1]:  # 자기 자신에 1을 더한 값과 앞의 요소의 값이 같으면 counts에 1을 더해줌
            counts += 1
        else:                           # 위의 조건이 아닐 경우 counts를 0으로 초기화
            counts = 1
        if counts > maxValue:           # counts가 maxValue보다 더 클 경우 maxValue에 할당
            maxValue = counts

    print(f'#{tc} {maxValue + 1}')  # 최소 길이 개수는 1이기 때문에 maxValue에 1을 더해줌