"""
1.아이디어
2차원 배열 a에 숫자더해야함
다중합
다중합 사용
2. 시간복잡도
n,m이 너무 크므로
다중합
3. 변수
배열 A[][]
다중합 저장 할 배열 B[][]
다중합 계산 배열 C[][]
"""
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=list(list(map(int,input().strip())))
B=list(list(map(int,input().strip())) for in range(m))
C=[[0]*n for _ in range(n)]
answer=0
for b in B:
    if b[0]==1:
        for j in range(b[2], b[4]):
            for i in range(b[0], b[3]):
                C[j][i]
    else :
        for j in range(n):
            for i in range(n):
                C[j][i]=
        for j in range(b[2],b[4]):
            for i in range(b[0],b[3]):
                answer+=A[j][i]
