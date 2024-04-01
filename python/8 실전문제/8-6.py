"""
1.아이디어
1이상 3이하의 정수를 외쳐야함
첫번째 학생은 1~2까지 외칠수 있음
그다음 학생은 1이면 2이상 3이하
2이면 3이상 4이하
첫번째 학생이 1이상 k 이하인 정수a를 외치고
두번째 학생이 a+1이상 a+k이하인 정수를 외쳐야함> 재귀함수
두번째 줄에는 외칠수 없는 정수 목록이 주어짐
정수를 못 외치면 진다.
외칠 수 있는 정수가 여러개면 그 중에 하나를 외친다.
2. 시간복잡도
3. 자료구조

"""
n,k=map(int,input().split())
A=list(map(int,input().split()))
def solution(n,k,A):
    B=[0]*(n+1)
    for a in A:
        B[a]=1
    return solve(n,k,0,B)
def solve(n,k,a,B):
    if a==n:
        return 0
    for b in range(a+1,a+k+1):
        if b>n:
            break
        if B[b]==1:
            continue
        if solve(n,k,b,B)==0:
            return 1
    return 0
print(solution(n,k,A))
