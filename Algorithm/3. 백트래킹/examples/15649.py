"""
1. 아이디어
- 백트래킹 재귀함수 안에서, for 문 돌면서 숫자 선택(방문여부확인)
- 재귀 함수에서 M개를 선택할 경우 print
2. 시간 복잡도
N! 가능
3. 자료구조
int[]
bool[]
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N + 1)


def recur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N + 1):
        if not chk[i]:
            chk[i] = True
            rs.append(i)
            recur(num + 1)
            chk[i]=False
            rs.pop()
recur(0)
