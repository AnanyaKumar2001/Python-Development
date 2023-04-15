x = [[1, 7],
     [4, 5],
     [7, 8]]

# -------------------------------------------------
# Approach One ->>>> Using Nested Loops
# result = [[0, 0, 0],
#           [0, 0, 0]]

# iterate through rows
# for row in range(len(x)):
#     # iterate over cols
#     for col in range(len(x[0])):
#         result[col][row] = x[row][col]

# print(result)

# for data in result:
#     print(data)


# -------------------------------------------------
# Approach Two ->>>> Nested LCE
result = [[x[col][row] for col in range(len(x))] for row in range(len(x[0]))]

print(result)
