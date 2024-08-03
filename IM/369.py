
def solution():    # 3,6,9 문제를 해결하기 위한 함수

    def viewCount(numbers, *args):
        viewcount = 0
        for n in numbers:
            if n in args:
                viewcount += 1
        return viewcount

    """
       :param numbers : 1~N까지의 숫자 배열
       :param args : 3,6,9
       :return
        viewcount numbers와 3,6,9를 비교하여 3,6,9의 개수를 리턴
    """

    N = int(input())
    newlist = []        # 빈 리스트를 만들어서
    for n in range(1,N+1):
        if viewCount(list(map(int, str(n))), 3,6,9) == 0:
            newlist += [n]
        else:
            newlist += ['-'* viewCount(list(map(int, str(n))), 3,6,9)]
    return newlist

answer = solution()

print(" ".join(map(str, answer)))











