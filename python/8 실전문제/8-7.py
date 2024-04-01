"""
1. 아이디어
규칙에 맞게 숫자를 외치면서
1)현재 학생이 이길수 있는 정수가 있으면 정수 개수 합이 최소
2)현재 학생이 이길수 있는 정수가 없으면 정수 개수의 합이 최대
3)현재 학생이 외칠수 있는 정수가 여러개이면 그중에 한개
두명의 학생이 외친 정수 개수의 합을 출력
2. 시간 복잡도
3. 변수
외칠수 없는 숫자 bool chk[i]

"""
def solution(n,k,A):
    B=[0]*(n+1)
    for a in A:
        B[a]=1
    return abs(solve(n,k,0,B))

def solve(n,k,a,B):
    if a==n:
        return 0
    nxt=[]
    for b in range(a+1,a+k+1):
        if b>n:
            break
        if B[b]==1:
            continue
        nxt.append(solve(n,k,b,B))
    if len(nxt)==0:
        return 0
    nxt.sort()
    if nxt[0]>0:
        return -(nxt[-1]+1)
    ret=None
    for i in range(len(nxt)):
        if nxt[i]<=0:
            ret=nxt[i]
    return -ret + 1
n,k=map(int,input().split())
A=list(map(int,input().split()))
print(solution(n,k,A))