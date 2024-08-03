T = int(input())
for tc in range(1,T+1):
    money = int(input())
    moneyList = [50000,10000,5000,1000,500,100,50,10] # 거스름돈의 종류를 구하기 위해 돈의 종류를 리스트로 만든다
    counts = [] # 거스름돈의 종류를 담을 빈 리스트 생성
    for m in moneyList: # 돈의 종류를 순회하면서
        if money // m == 0:  # 입력받은 돈을 각각 나눈 값이 0이면 0을 추가
            counts += [0]
        else:                # 0이 아닐 때는
            counts += [money // m]   # 입력받은 돈에서 거스름돈의 종류를 나눈 몫이 종류의 개수이기 떄문에 리스트에 추가
            money %= m                    # 돈을 거스름돈의 종류로 나눈 나머지를 money에 할당하여 그 돈으로 다시 for문 반복
    print(f'#{tc}')
    print(' '.join(map(str, counts)))