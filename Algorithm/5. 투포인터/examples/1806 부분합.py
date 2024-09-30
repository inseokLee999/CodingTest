"""
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.
예제 입력 :
10 15
5 1 3 5 10 7 4 9 2 8
1. 아이디어
1부터 커지면서
for 문을 돌면서  S 이상이 되는게 있는지 체크
2. 시간 복잡도
for 문 n O(n)
최대 O(n^2) 넘는다
투포인터
3. 갯수 cnt
"""
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
sum = 0
presum = 0

def solution(N, S, nums):
    presum = nums[0]
    for i in range(1, N + 1):
        sum = presum
        presum += nums[i]
        if sum >= S:
            return i
        for j in range(N - i):
            sum -= nums[j]
            sum += nums[j + i]
            if sum >= S:
                return i
    return 0


print(solution(N, S, nums))
