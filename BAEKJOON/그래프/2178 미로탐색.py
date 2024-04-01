"""
1. 아이디어
(N,M)에 도착했을 때 이동값 중 최솟값
1인경우 min_cnt(i)=min(min_cnt,min_cnt(i-1)) 값 갱신
2. 시간복잡도
N*M
3. 변수
min_cnt[N][M]=INF
"""
from collections import deque
N,M=map(int,input().split())
A=list(input().strip() for _ in range(N))
maze=[[]*M for _ in range(N)]

for j in range(N):
    for i in range(M):
        maze[j].append(int(A[j][i]))

def bfs(maze, N, M):
    dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 x 방향 변화량
    dy = [0, 0, -1, 1]  # 상하좌우 이동을 위한 y 방향 변화량

    queue = deque([(0, 0, 1)])  # 시작 위치와 이동한 칸 수를 저장하는 큐
    visited = [[False] * M for _ in range(N)]  # 방문 여부를 저장하는 배열
    visited[0][0] = True  # 시작 위치를 방문했다고 표시

    while queue:
        x, y, count = queue.popleft()

        # 도착 위치에 도달하면 칸 수를 반환
        if x == N - 1 and y == M - 1:
            return count

        # 상하좌우 이동을 확인하여 갈 수 있는 칸을 큐에 추가
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True

    return -1  # 도착 위치까지 도달할 수 없는 경우

result = bfs(maze, N, M)
print(result)
