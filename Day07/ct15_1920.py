# 백준 1920 - 원하는 정수 찾기
N = int(input()) # 5
A = list(map(int, input().split())) # 4 1 5 2 3
A.sort() # 파이썬 리스트에서 제공하는 기본 정렬

M = int(input()) # 4
targetList = list(map(int, input().split())) # 1 3 7 9

for i in range(M):
    find = False
    target = targetList[i]
    # 이진탐색

    start = 0
    end = N - 1
    while start <= end:
        midle = (start + end) // 2
        midVal = A[midle]
        if midVal > target:
            end = midle - 1
        elif midVal < target: # 왼쪽 날림
            start = midle + 1
        else: # 값을 찾는 것
            find = True
            break

if find:
    print(1)
else:
    print(0)