x = [[9, 5, 2],
     [4, 8, 6],
     [7, 3, 1]]

y = [[1, 9, 1, 11],
     [2, 6, 5, 7],
     [3, 4, 1, 5]]

# -----------------------------------
# Approach One ->>>> Nested Loop

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# iterating through rows of x
for i in range(len(x)):
    # iterating through cols of y
    for j in range(len(y[0])):
        # iterating through rows of y
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

print(result)


# -----------------------------------
# Approach Two ->>>> Nested LCE

result = [[sum(a * b for a, b in zip(x_row, y_col))
           for y_col in zip(*y)] for x_row in x]

print(result)
