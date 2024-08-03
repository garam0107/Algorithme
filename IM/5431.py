T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))
    people = list(range(N+1))   # 수강생들의 번호는 1~N이기 때문에 N+1까지 생성, arr과 비교하기 위한 리스트
    Worklist = set()  # 빈 세트를 2개 만드는 이유는 차집합으로 풀기 위함
    total = set()

    for work in arr:      #arr의 요소를 순회 하면서 people안에 있을때
        if work in people:
            Worklist.add(people[int(work)])   # Worklist의 추가
    for i in range(1,N+1):        # 전체 수강생의 번호가 존재하는 set 생성
        total.add(i)

    notAssign = total - Worklist      # 전체 수강생 번호가 있는 set total와 과제를 한 수강생의 set Worklist의 차집합
    print(f'#{tc} {" ".join(map(str, notAssign))}')    # 세트를 문자열로 나타내기 위해 join을 이용해 출력

# 세트말고 리스트로 내장함수 안쓰고 풀어보기














