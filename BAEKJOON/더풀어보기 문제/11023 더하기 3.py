import sys
input=sys.stdin.readline

A=list(map(int,input().split()))
answer=0
for a in A:
    answer+=a
print(answer)