import sys
input=sys.stdin.readline
A=int(input())
Coins=[500,100,50,10]
count=0
for coin in Coins:
    count+=(A//coin)
    A%=coin
print(count)