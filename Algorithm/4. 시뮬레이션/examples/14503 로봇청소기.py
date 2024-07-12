"""
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 방은 NXM 크기의 직사각형으로 나타낼 수 있으며, $1 \times 1$ 크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 방의 각 칸은 좌표 $(r, c)$로 나타낼 수 있고, 가장 북쪽 줄의 가장 서쪽 칸의 좌표가 $(0, 0)$, 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 $(N-1, M-1)$이다. 즉, 좌표 $(r, c)$는 북쪽에서 $(r+1)$번째에 있는 줄의 서쪽에서 $(c+1)$번째 칸을 가리킨다. 처음에 빈 칸은 전부 청소되지 않은 상태이다.

로봇 청소기는 다음과 같이 작동한다.

현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
반시계 방향으로 $90^\circ$ 회전한다.
바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
1번으로 돌아간다.
1. 아이디어
특정 조건 만족 하는 한 계속 이동 while
4방향 탐색 먼저 수행 > 빈칸있을 경우 이동
4방향 탐색 안될경우 뒤로 한칸 가서 반복
2. 시간복잡도
while 문 N*M*4
3. 자료구조
int[][]
내위치 방향 int,int,int +1%4
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))

cnt = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# def calculate
def solution(r, c, d, board):
    global cnt
    while True:
        board[r][c] = 2
        cnt += 1

        for i in range(4):
            nr = r + dy[(i + d) % 4]
            nc = c + dx[(i + d) % 4]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] != 0:
                    if i != 3:
                        continue
                    elif board[r + dy[(d + 2) % 4]][c + dx[(d + 2) % 4]] != 1:
                        r = r + dy[(d + 2) % 4]
                        c = c + dx[(d + 2) % 4]
                        break
                    elif board[r + dy[(d + 2) % 4]][c + dx[(d + 2) % 4]] == 1:
                        return cnt
                elif board[nr][nc] == 0:
                    r = nr
                    c = nc
                    d = (d + i) % 4
                    print("r : %d, c: %d, d : %d" % (r, c, d))
                    break

    return cnt


print(solution(r, c, d, board))
