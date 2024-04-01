import sys
input=sys.stdin.readline
N = int(input())
A=input().strip()
sum=0
for a in A:
    sum+=int(a)
print(sum)