"""
1. 아이디어
제일 적은 시간걸리는 순서대로 뽑는다
2. 시간 복잡도
그냥 가장 작은거 하면 O(N^2)
sort하고 하면 O(logN)
3. 변수
걸린 시간
"""
import sys
input=sys.stdin.readline
N=int(input())
P=list(map(int,input().split()))
time_sum=P[0]
P.sort()
DP=[P[0]]
for i in range(1,N):
    DP.append(DP[i-1]+P[i])
print(sum(DP))