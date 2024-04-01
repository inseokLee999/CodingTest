"""
1. 아이디어
combination 사용하여 C(X,k),C(Y,k),C(Z,k) (tuple)생성
C 하나씩 검사하여 D에 다가 횟수+1
두번이상 나타나는 문자열을 answer=[]에 저장후 오름차순 으로 저장
2. 시간 복잡도
C(17,k) 72930
3. 자료구조
Tuple X,Y,Z()
Dictionary ={}
answer=[]
"""
from itertools import combinations
X=input().strip()
Y=input().strip()
Z=input().strip()
k=int(input())
def solve(Tuple_X, D):
    for x in Tuple_X:
        if x in D:
            D[x]+=1
        else :
            D[x]=1
def solution(X,Y,Z,k):
    Tuple_X, Tuple_Y, Tuple_Z = combinations(X,k), combinations(Y,k), combinations(Z,k)
    D={}
    answer=[]
    solve(Tuple_X, D)
    solve(Tuple_Y, D)
    solve(Tuple_Z, D)

    for key,value in D.items():
        if value>=2:
            answer.append(''.join(list(key)))
    answer.sort()
    return answer
C=solution(X,Y,Z,k)
if len(C)==0:
    print(-1)
else:
    for c in C:
        print(c)