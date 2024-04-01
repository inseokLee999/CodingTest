"""
1. 아이디어
제일 비싼것 부터 다 넣고
순서 대로 최대한 넣는다
그리디?
2. 시간 복잡도
O(N)= 10^6
nlogn 2*10*7
3. 변수
전체 W
남은 무게 remain=
금액 price
"""
import sys
input=sys.stdin.readline
W,N=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
A.sort(key=lambda x:-x[1])
price=0
remain=W
for i in range(N):
    if remain>0:
        if remain >= A[i][0]:
            remain -= A[i][0]
            price+=A[i][0]*A[i][1]
        elif (remain<A[i][0]):
            price+=remain*A[i][1]
            remain = 0
print(price)


