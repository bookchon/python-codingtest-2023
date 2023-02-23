# 백준 1197 - 최소 신장 트리
# 시간복잡도 0(e*log(e))
import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N+1)


# 유니온 파인드를 위한 대표 노드 리스트 초기화
for i in range(N+1):
    parent[i] = i

for i in range(M): # 엣지 갯수만큼 입력
    s, e, w = map(int, input().split())
    pq.put((w, s, e)) # 가중치 중심 정렬

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b): # 두 노드 연결
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

result = 0

for _ in range(N - 1): # MST N-1에서 여기까지
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w

print(result)