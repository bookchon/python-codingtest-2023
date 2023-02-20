# 백준 12891 - dna 비밀번호

checkList = [0] * 4 # ACGT 유전자 값
myList = [0] * 4 # 부분 문자열의 ACGT 갯수
checkSecret = 0

# 함수
def myadd(c): # 새로 들어온 문자를 처리
    global checkList, myList, checkSecret
    if c == 'A' :
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == "C":
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkList += 1
    elif c == "G":
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkList += 1
    elif c == "T":
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkList += 1

def myremove(c): # 제거되는 문자 처리
    global checkList, myList, checkSecret
    if c == 'A' :
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == "C":
        if myList[1] == checkList[1]:
            checkList -= 1
        myList[1] -= 1
    elif c == "G":
        if myList[2] == checkList[2]:
            checkList -= 1
        myList[2] -= 1
    elif c == "T":
        if myList[3] == checkList[3]:
            checkList -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P): # 부분 문자열 갯수 만큼
    myadd(A[i])

if checkSecret == 4: # ACGT
    Result += 1

for i in range(P, S): # 2, 4
    j = i - P # 2 - 2 = -2
    myadd(A[i]) # 이번 슬라이드에서 처리된 값을 추가
    myremove(A[j]) # 이전 슬라이드에서 처리한 값을 제거
    if checkSecret == 4:
        Result += 1

print(Result)