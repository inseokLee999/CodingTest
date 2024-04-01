import sys
input=sys.stdin.readline
N=int(input())
DP=list([0]*(N+1))
DP=[0,0,1]
for i in range(3,N+1):
    if i%3==0 and i%2==0:
        DP.append(min(DP[i//3]+1,DP[i//2]+1,DP[i-1]+1))
        continue
    elif i%3==0:
        DP.append(min(DP[i//3]+1,DP[i-1]+1))
        continue
    elif i%2==0:
        DP.append(min(DP[i//2]+1,DP[i-1]+1))
        continue
    else :
        DP.append(DP[i-1]+1)
        continue
print(DP[N])