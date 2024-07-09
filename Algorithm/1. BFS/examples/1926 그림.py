"""
https://www.acmicpc.net/problem/1926
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자.
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)
예제 입력 :
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

1. 아이디어
2중 for => 값 1 && 방문X ->BFS
그림개수 +1 최대값 반환
2. 시간복잡도
O(V+E)
V= M*N =500*500
E = 4*500*500
V+E = 100만 < 2억 가능
3. 자료구조
그래프 전체 지도 int [][]
방문 bool[][]
queue
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
cnt = 0
maxv = 0
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and not chk[ny][nx]:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs


for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체그림 개수 +1
            cnt += 1
            # BFS: 그림크기
            maxv = max(maxv, bfs(j, i))
print(cnt)
print(maxv)
