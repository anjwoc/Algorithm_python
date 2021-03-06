import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


def counting(x, y):
    global visited, maps
    visited[x][y] = True

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        if visited[nx][ny]:
            continue

        if maps[nx][ny]:
            visited[nx][ny] = True
            counting(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit(0)
    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j]:
                counting(i, j)
                ans += 1
    print(ans)
