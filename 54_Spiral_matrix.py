# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:


# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
# Example 2:


# Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

def spiralOrder(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    top, left, down, right = 0, 0, rows - 1, columns - 1
    d = 0
    res = []
    while top <= down and left <= right:

        ## left --> right
        if d == 0:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            # print(res)

        ## top --> down
        if d == 1:
            for i in range(top, down+1):
                res.append(matrix[i][right])
            right -= 1
            # print(res)

        ## right --> left
        if d == 2:
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            # print(res)

        ## down --> top
        if d == 3:
            for i in range(down, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            # print(res)
        d = (d+1) % 4
    return res
