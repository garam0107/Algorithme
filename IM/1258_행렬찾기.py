def row(r,c):






def procession(array,N):
    sr,sc = 0,0
    counts = 0
    process_list = []
    while sc < N:
        if array[sr][sc] != 0:
            counts += 1
            sc += 1
        else:
            break


    return process_list,sc



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    print(procession(array,N))
