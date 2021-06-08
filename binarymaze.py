import sys


# Check if it is possible to go to `(x, y)` from the current position. The
# function returns false if the cell has value 0 or already visited
def isSafe(mat, visited, x, y):
    return not (mat[x][y] == 0 or visited[x][y])


# Returns false if not a valid position
def isValid(x, y):
    return M > x >= 0 and N > y >= 0


# Find the shortest possible route in a matrix `mat` from source cell `(0, 0)`
# to destination cell `(x, y)`.

# `min_dist` stores the length of the longest path from source to a destination
# found so far, and `dist` maintains the length of the path from a source cell to
# the current cell `(i, j)`.

def findShortestPath(mat, visited, i, j, x, y, min_dist, dist):

    # if the destination is found, update `min_dist`
    if i == x and j == y:
        return min(dist, min_dist)

    # set `(i, j)` cell as visited
    visited[i][j] = 1

    # go to the bottom cell
    if isValid(i + 1, j) and isSafe(mat, visited, i + 1, j):
        min_dist = findShortestPath(mat, visited, i + 1, j, x, y, min_dist, dist + 1)

    # go to the right cell
    if isValid(i, j + 1) and isSafe(mat, visited, i, j + 1):
        min_dist = findShortestPath(mat, visited, i, j + 1, x, y, min_dist, dist + 1)

    # go to the top cell
    if isValid(i - 1, j) and isSafe(mat, visited, i - 1, j):
        min_dist = findShortestPath(mat, visited, i - 1, j, x, y, min_dist, dist + 1)

    # go to the left cell
    if isValid(i, j - 1) and isSafe(mat, visited, i, j - 1):
        min_dist = findShortestPath(mat, visited, i, j - 1, x, y, min_dist, dist + 1)

    # backtrack: remove `(i, j)` from the visited matrix
    visited[i][j] = 0

    return min_dist


if __name__ == '__main__':

    mat = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]

    M = N = 10

    # construct a matrix to keep track of visited cells
    visited = [[0 for x in range(N)] for y in range(M)]

    min_dist = findShortestPath(mat, visited, 0, 0, 7, 5, sys.maxsize, 0)

    if min_dist != sys.maxsize:
        print("The shortest path from source to destination has length", min_dist)
    else:
        print("Destination can't be reached from source")
