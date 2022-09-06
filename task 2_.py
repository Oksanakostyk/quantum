from collections import deque
import numpy as np

# all possible movements in 8 directions
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


# Check function for safe transition to position (x, y)


def can_move(mat, x, y, processed):
    return (x >= 0 and x < len(processed)) and (y >= 0 and y < len(processed[0])) and \
           mat[x][y] == 1 and not processed[x][y]


def BFS(mat, processed, i, j):
    q = deque()
    q.append((i, j))

    processed[i][j] = True

    while q:
        x, y = q.popleft()
        for k in range(len(row)):

            if can_move(mat, x + row[k], y + col[k], processed):
                processed[x + row[k]][y + col[k]] = True
                q.append((x + row[k], y + col[k]))


def count_islands(mat):
    if not mat or not len(mat):
        return 0


    processed = [[False for x in range(N)] for y in range(M)]

    island = 0
    for i in range(M):
        for j in range(N):

            if mat[i][j] == 1 and not processed[i][j]:
                BFS(mat, processed, i, j)
                island = island + 1
    return island


if __name__ == '__main__':
    N, M = (int(x) for x in input('Enter N M').split())
    mat = []
    for i in range(N):
        i = [int(x) for x in input().split()]
        mat = np.append([mat],[i])

    mat=np.reshape(mat, (N, M))
    mat=deque(mat)



    print(count_islands(mat))
