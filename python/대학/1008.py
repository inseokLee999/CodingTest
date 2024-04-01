n=int(input())
A=list(list(map(int,input().split()))for _ in range(n))
answer=[]
for a in A:
    answer.append((sum(a[0:5])/5,a[5]))
answer.sort(key=lambda x:(-x[0],x[1]))
for i in answer:
    print(i[1])