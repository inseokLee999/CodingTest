"""
1.아이디어
n->k진수로 변환 해주는 함수 digit(n,k) 10진수 str로 리턴
for 문으로 0부터 끝까지
0 아닌 시작 부터 0까지
b에다가 int변환 후 추가
다 더한후 다시 digit 함수로 변환
2. 시간복잡도
가능
3. 변수
집합 B
n->k변환 수 num_str
"""
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
B=list()
def digit(n,k):
    i=0
    answer=0
    while n>0:
        d=n%k
        n//=k
        answer+=d*(10**(i))
        i+=1
    return answer
num_str=str(digit(n,k))
for i in num_str.split('0'):
    if i!='':
        B.append(int(i))
sum=0
for b in B:
    sum+=b
print(digit(sum,k))