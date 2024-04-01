import sys
input=sys.stdin.readline
N=int(input())
A=[]
for i in range(N):
    S,T=map(int,input().split())
    A.append([S,T])
A.sort(key=lambda x:(x[1],x[0]))
num=0#회의의 수
finish=0
for a in A:
    if finish<=a[0]:
        num+=1
        finish=a[1]
print(num)