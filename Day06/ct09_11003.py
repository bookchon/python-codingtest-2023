# 백준 11003 - 최솟값 찾기1
from collections import deque
from pythonds.basic.deque import Deque

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split())) # 1 5 2 3 6 2 3 7 3 5 2 6


# 새 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거하여 시간 복잡도를 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # 인덱스가 현재값보다 크면
        mydeque.pop() # 빼는 것
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L: # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end= ' ') # 이 값은 무조건 최소값(min() 함수를 쓰는 것과 똑같음)
