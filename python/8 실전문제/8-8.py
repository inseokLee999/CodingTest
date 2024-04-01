"""
1. 아이디어
P(A)가 주어지면
for 문으로 돌면서
P(A)<P(B)를 만족하는 P(B)를 리스트에 추가

백트래킹
2. 시간복잡도 9^n 가능
3. 변수
B 집합 리스트

"""
n=int(input())
A=list(map(int,input().split()))
PA=1
for a in A:
    PA*=a
B=[]
result=[]
def recur(num):
    if num==n:
        mul=1
        for rs in result:
            mul*=rs
        if mul>PA:
            B.append(list(result))
        return
    for i in range(1,10):
        result.append(i)
        recur(num+1)
        result.pop()

recur(0)

if len(B)==0:
    print(-1)
else :
    for i in B[0]:
        print(i,end=' ')