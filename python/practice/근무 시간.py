"""
1. 아이디어
문자열을 받아서 정수형으로 전환후 합
2.시간 복잡도
O(N)
3. 변수
시간 변환 함수,
총합 int
"""
import sys
input = sys.stdin.readline
A=[list(input().split())for _ in range(5)]
sum=0
def translate_time(S):
    return 60*(int(S[:2])) + int(S[3:])
for a in A:
    sum+=translate_time(a[1])-translate_time(a[0])
print(sum)


