"""
처음아이디어 for 문으로 각 숫자의 위치에서 이후 k개의 수를 더함
이때 마다 최대값으로 갱신
시간복잡도 : O(N)
O(N*k)
10만 * 10만 = 1 e10 초과함

처음에 K 개 값을 구함
for 문 다음인덱스 값 더하고 앞의값을 뺌
O(N)*2
O(2N)

1. 아이디어
투포인터
for 문 처음 k 값 저장
다음인덱스 더하고 이전 인덱스 빼줌
최댓값 갱신
2. 시간복잡도
3. 자료구조 각 숫자들 N개 저장 Int[]
최댓값, k값 저장 변수
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
each = 0
# k개 더해주기
for i in range(K):
    each += nums[i]
maxv = each

# 다음 더하고 이전인덱스 빼주기
for i in range(K, N):
    each += nums[i]
    each -= nums[i - K]
    maxv = max(each, maxv)
print(maxv)