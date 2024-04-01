"""
1. 아이디어
for 문으로 한글자 씩 대입하며 초염기 서열을 만들며 pop
2. 시간 복잡도
O(M*N)
3.변수
염기 서열 리스트 str[]
"""
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
A=list(input().strip() for _ in range(N))
cnt=0
superb=[]

while A:
    temp = list(A.pop())
    temp_str = ''.join(temp)
    for a in A:
        for i in range(M):
            if i==M-1 and (a[i]==temp[i] or temp[i]=='.'):
                A.remove(a)
                superb.append(temp_str)
            elif a[i]==temp[i] or a[i]=='.':
                continue
            elif temp[i]=='.':
                temp[i]=a[i]

            else :
                break
print(len(superb),superb)




