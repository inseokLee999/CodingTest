"""
2.시간 복잡도
N(B)
"""
A,B,C=map(int,input().split())
B%=C
num=1
rs=[]
for i in range(B):
    num*=A
    num%=C
print(num)