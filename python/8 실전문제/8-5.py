"""
1. 아이디어
두 명의 학생이 번갈아가면서 사과를 먹는다.
상하좌우 한칸이동하고
장애물있는칸으로 x
해당칸을 떠나는 즉시 장애물 있는 칸
방문/ 장애물 표시는 A->-1
다른학생이 있는 칸으로 갈수 없음
이동할수 없으면 다른학생으로 이동기회가 넘어감
모두 이동할수 없거나 사과를 모두 먹으면 게임 종료 while 문으로
두명의 학생은 최고로 먹도로 플레이
최적의 플레이를 했을 때 첫번째가 두번째보다 많이먹으면 1, 그렇지 않으면 0
2. 시간복잡도
bfs O(v+e)=5V 125
3. 자료구조
A= int [5][5] 보드 5x5
사과 먹은 갯수 num_A,num_B
A 위치[][]
B 위치 [][]
차이 answer
답 maxv
"""
A = list(list(map(int, input().split())) for _ in range(5))
y1, x1, y2, x2 = map(int, input().split())
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
answer = 0


def in_range(y, x):
    return 0 <= y <= 4 and 0 <= x <= 4


def cannot_move(Y, X):
    for i in range(4):
        ny = Y + dy[i]
        nx = X + dx[i]
        if (in_range(ny, nx) == True and A[ny][nx] != -1):
            return False
    return True


def solution(A, y1, x1, y2, x2):
    apple_num = 0
    for j in range(4):
        for i in range(4):
            if A[j][i] == 1:
                apple_num += 1
    current_x1, current_y1 = x1, y1
    current_x2, current_y2 = x2, y2

    apple_1 = 0
    apple_2 = 0
    while ((cannot_move(current_y1, current_x1) and cannot_move(current_y2, current_x2)) or apple_num == 0) != True:
        for i in range(4):
            ny1 = current_y1 + dy[i]
            nx1 = current_x1 + dx[i]
            if cannot_move(ny2, nx1) != True:  # 움직일수 있으면
                A[current_y1][current_x1] = -1  # 그전에 있던곳 -1
                current_y1 = ny1  # 현재 위치 업데이트
                current_x1 = nx1
                if A[current_y1][current_x1] == 1:  # 현재위치에 사과가 있으면
                    apple_num -= 1  # 전체사과 -1
                    apple_1 += 1  # 먹은사과 +1
            ny2 = current_y


