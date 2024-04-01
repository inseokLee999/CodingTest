import sys
input = sys.stdin.readline
T=int(input())
k=list()
n=list()
room=list([0]*15 for _ in range(15))
for i in range(15):
    room[0][i]+=i
for i in range(T):
    k.append(int(input()))
    n.append(int(input()))
for j in range(1,15):
    for i in range(1,15):
        room[j][i]=room[j-1][i]+room[j][i-1]
for i in range(T):
    a=k[i]
    b=n[i]
    print(room[a][b])
