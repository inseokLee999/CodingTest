N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
answer = 0
for i in range(N):
    answer += A[i] * B.pop(B.index(max(B)))
print(answer)
