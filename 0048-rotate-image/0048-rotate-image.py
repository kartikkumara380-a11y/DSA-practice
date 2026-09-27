class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        a = [[0] * row for _ in range(col)]
        for i in range(0, row):
            for j in range(0, col):
                a[j][i] = matrix[i][j]
        for i in range(row):
            a[i].reverse()
        for i in range(row):
            matrix[i] = a[i]