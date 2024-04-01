"""
1. 아이디어
2차원 배열 을 사용해서 m[n][3] 을 작성해서 저장
질문 1당 과목 과일 색깔에 대해 모두 일치 하는 학생 카운트

2. 시간복잡도
O(m*n)=10^6
3. 알고리즘
2차원 배열 string[][]
질의 [].split()
"""
n,m=map(int,input().split())
A=list(list((input().split()))for _ in range(n))
B=list(list((input().split()))for _ in range(m))
def solution(n,m,A,B):
    for b in B:
        cnt=0
        for i in range(n):
            if b[0] == A[i][0] or b[0] == '-':
                if b[1] == A[i][1] or b[1] == '-':
                    if b[2] == A[i][2] or b[2] == '-':
                        cnt += 1
        print(cnt)
solution(n,m,A,B)