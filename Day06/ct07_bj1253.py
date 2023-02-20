# 백준 1253

import sys
input = sys.stdin.readline

N = int(input())
count = 0
A = list(map(int, input().split())) # 한 줄에 입력 다 받음
A.sort() # 전체 정렬

for k in range(N):
    find = A[k] 
    i = 0; j = N - 1 # i는 리스트 첫번째, j는 리스트 마지막번째 위치를 잡음
    while i < j: # 두 인덱스가 만나면 while문 종료
        if A[i] + A[j] == find: # 두 수의 합이 차즌ㄴ 수와 일치할 때
            if i != k and j != k: # i, j는 k와 같은 위치가 되면 안됨
                count += 1
                break
            elif i == k: i += 1
            elif j == k: j -= 1
        elif A[i] + A[j] < find : # 두 수를 합산한 값이 find보다 작은 경우 i를 증가시켜 합의수를 크게 함
            i += 1
        elif A[i] + A[j] > find: # j의 수를 감소시켜야 합의 수가 작아짐
            j -= 1
print(count)