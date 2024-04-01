"""
1. 아이디어
학생들 명단 배열을 받고
차례대로 dictionary 에 인기도 +1
dict 를 배열로 받고 정렬
2. 시간복잡도
O(n*n+nlogn)=n*n
3. 자료구조
인기도 dictionary={}

"""
n=int(input())
A=list(input().split())
B=list(list(input().split()) for _ in range(n))
def solution(n,A,B):
    D={}
    popul=[]
    for a in A:
        D[a]=0
    for b in B:
        for name in b:
            D[name]+=1
    answer=list(D.items())
    answer.sort(key=lambda x:(-x[1],x[0]))
    return answer
C=solution(n,A,B)
for name,value in C:
    print(name,value)