# 백준 11724 - 연결 요소 갯수 확인
import sys
# 재귀호출 파이썬 제한 1,000번 까지 가능
sys.setrecursionlimit(10 ** 6) # 1,000,000
input = sys.stdin.readline # 입력받는 속도가 느리기 때문에 백준에서 그냥 돌리면 오류 남
n, m = map(int, input().split()) # 6, 5
A = [[] for _ in range(n+1)] # x, 7열 2차원 리스트
visited = [False] * (n+1) # [0, 1, 2, 3, 4, 5, 6]


# DFS 함수(재귀함수)
def DFS(v):
    visited[v] = True # 방문 노드를 참으로 바꿈 (원래 flase)
    for i in A[v]:
        if not visited[i]: # 만약 i 값이 방문하지 않았다면
            DFS(i)

for _ in range(m): # 엣지 갯수만큼 돎
    s, e = map(int, input().split())
    A[s].append(e) # 무방향이기 때문에 양쪽 엣지 추가
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)