'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.
도착할 수 있으면 1, 아니면 0을 출력한다. 주어진 미로 밖으로는 나갈 수 없다.

다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나
 또는 ‘error’를 출력한다.
'''
import sys
sys.stdin = open("2_미로", "r")

def check(x, y):
    if x < 0 or x > N-1 : return False
    if y < 0 or y > N-1 : return False
    if maze[x][y] == 1  : return False
    return True


def DFS(x, y):
    stack = [0] * (N*N)
    top = -1

    top += 1
    stack[top] = x, y

    while top != -1:
        x, y = stack[top] ; top -= 1

        if maze[x][y] == 3 : return 1
        if maze[x][y] != 1 :
            maze[x][y] = 1
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if check(newX, newY) :
                    top += 1 ; stack[top] = newX, newY
    return 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                sX = i
                sY = j

    print('#%d'%tc, DFS(sX, sY))




# import sys
# sys.stdin = open("input.txt", "r")
#
# def DFSr(x, y):
#     global found
#     if not 0 <= x < N or not 0 <= y < N or found or maze[x][y] == 1 : return
#     if maze[x][y] == 3 : found = 1; return
#
#     maze[x][y] = 1
#     DFSr(x, y+1)
#     DFSr(x, y-1)
#     DFSr(x+1, y)
#     DFSr(x-1, y)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     maze = [[int(x) for x in input()] for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2 :
#                 sX = i
#                 sY = j
#
#     found = 0
#     DFSr(sX, sY)
#     print('#%d'%tc, found)