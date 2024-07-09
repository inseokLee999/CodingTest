"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
예제 입력 :
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 :
3
7
8
9
1. 아이디어 :
- 2중 for 문, 값 1 && 방문 X => DFS
찾은 값 저장후 정렬해서 출력
2. 시간복잡도 :
O(V+E): N^2 :625
3. 자료구조 :
그래프 저장 int 값
방문 여부 : bool[][]
결과 값 : int []


"""
import sys

input = sys.stdin.readline

N = int(input())
map = [[] * N for _ in range(N)]
for i in range(N):
    for j in input().split():
        for k in j:
            map[i].append(int(k))

print(map)
chk = [[False] * N for _ in range(N)]
result = []
each = 0

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if map[ny][nx] and not chk[ny][nx]:
                chk[ny][nx] = True
                dfs(ny, nx)


for j in range(N):
    for i in range(N):
        if map[j][i] and not chk[j][i]:
            chk[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)
