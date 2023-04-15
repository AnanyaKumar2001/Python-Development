
x = [[1, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]


y = [[1, 9, 1],
     [6, 7, 3],
     [4, 5, 9]]

# -------------------------------------------
# Approach One ->>>> Nested Loop

# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]


# for row in range(len(x)):
#     for col in range(len(x[0])):
#         result[row][col] = x[row][col] + y[row][col]


# print(result)


# -------------------------------------------
# Approach Two ->>>> Nested LCE

result = [[x[row][col] + y[row][col]
           for col in range(len(x[0]))] for row in range(len(x))]

print(result)
