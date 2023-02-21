# 백준 1929 - 소수구하기
import math
M, N = map(int, input().split())
A = [0] * (N+1) # 초기화

for i in range(2, N+1):
    A[i] = i # 인덱스를 채워넣기

for i in range(2, int(math.sqrt(N))): # N의 제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i+1, N+1, i):
        A[j] = 0 # 소수가 아님

for i in range(M, N+1):
    if A[i] != 0:
        print(A[i])