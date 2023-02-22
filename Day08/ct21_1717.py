# 백준 1717 - 집합의 표현
# union-Find 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
N, M = map(int, input().split())
parent = [0] * (N + 1) # [0 for _ in range(N+1)]


def find(a): # find 연산
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀호출 -> 경로압축 (시간 복잡도를 줄임)
        return parent[a]

def union(a, b): # 대표 노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b: # a와 b가 같지 않으명
        parent[b] = a # b를 a랑 합침

def checkSame(a, b): # 둘이 같은 집합인지 확인
    a = find(a)
    b = find(b)
    if a == b: return True
    else : return False

for i in range(0, N+1):
    parent[i] = i 

for i in range(M):
    question, a, b = map(int, input().split()) # 0 1 3 or 1 1 7
    if question == 0:
        union(a, b)
    else:
        if checkSame(a,b):
            print('yes')
        else:
            print('No')