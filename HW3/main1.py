
rows = 4
cols = 6
array2 = (lambda rows, cols :   [[(i_rows + 1) * (i_cols + 1) for i_cols in range(cols)] for i_rows
          in range(rows)])(4,6)

print(array2)
