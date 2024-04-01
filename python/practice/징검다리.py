"""
1. 아이디어
for 문으로 처음 부터 확인
2. 시간 복잡도 아마 n^2 9*10^6
3. 변수
돌 int[]
chk []

"""
import sys
input= sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
chk=[1]*N
count=[1]*N
maxA=max(A)
maxv=0
def recur(num,cnt):
    global maxv
    while (num <N):
        for i in range(num + 1, N):
            if A[num] < A[i]:  # 더 큰 수가 나오면
                if chk[num] < cnt:  # chk 값도 크면
                    chk[num] = cnt + 1
                    recur(i, cnt + 1)
                else:
                    return
        break
    maxv = max(maxv, cnt)
    print("maxv update", num + 1,cnt)
    return
for i in range(N):
    if chk[i]==1:
        print("recur실행 ",i+1)
        recur(i,1)


print(maxv)