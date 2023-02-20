N = int(int())
A = [0] * int(N + 1)

for i in range(1, N+1):
    A[i] = int(input())

A = sorted(A, reverse=False)

for i in range(1, N+1):
    print(A[i])