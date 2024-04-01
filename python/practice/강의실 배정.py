import sys
input = sys.stdin.readline
N = int(input())
A = []
cnt = 0
for i in range(N):
    s, f = map(int, input().split())
    A.append([f,s])
A.sort()
D={}
chk={}
maxv=0
for a in A:
    if a[0] in D:
        D[a[0]].append(a[1])
    else :
        D[a[0]]=[a[1]]
def return_value(num):
    for i in range(num):
        if num-i in chk:
            return chk[num-i]
    return 0
def chk_start(num):
    if num not in chk:
        return return_value(num)
    else :
        return chk[num]
for key, value in D.items():
    for v in value:
        if key not in chk:
            chk[key]=max(return_value(key),chk_start(v)+1)
        else :
            chk[key]=max(chk[key],chk_start(v)+1)
        maxv=max(chk[key],maxv)


print(maxv)
