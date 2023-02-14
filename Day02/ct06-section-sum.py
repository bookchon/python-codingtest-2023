# 2차원 구간 합
# 백준 - 11660번
import sys
input = sys.stdin.readline
n, m = tuple(map(int, input().split())) # 2차원 행렬 크기, 질의 갯수
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]
# 2차원 구간합 구하기
for i in range(n):
    rows = list(map(int, input().split()))
    A_row = [0] + rows
    A.append(A_row)
# 2차원 합배열 D 만들기 / O(1024X1024) 백만 정도의 처리만 진행
for i in range(1, n+1):
    for j in range (1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
# 구간 합 구하기
for _ in range(m): # 언더바(_)는 반복에 들어오는 변수를(0,1,2) 값을 쓰지 않겠다는 이야기
    x1, y1, x2, y2 = map(int, input().split())
    result =  D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)