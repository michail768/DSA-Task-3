def represent_sparse(matrix):
  sparse_matrix = []
  rows = len(matrix)
  cols = len(matrix[0])

  # First row stores total rows, total columns, and total non-zero values
  non_zeros = 0
  for r in range(rows):
    for c in range(cols):
      if matrix[r][c] != 0:
        non_zeros += 1
        sparse_matrix.append([r, c, matrix[r][c]])

  sparse_matrix.insert(0, [rows, cols, non_zeros])
  return sparse_matrix


# Example Usage:
mat = [[0, 0, 3], [4, 0, 0], [0, 5, 0]]
print(represent_sparse(mat))
# Output: [[3, 3, 3], [0, 2, 3], [1, 0, 4], [2, 1, 5]]