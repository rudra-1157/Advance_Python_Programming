# Unique Paths using Dynamic Programming (Tabulation)

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))


dp = [[0 for j in range(cols)] for i in range(rows)]


for i in range(rows):
    dp[i][0] = 1

for j in range(cols):
    dp[0][j] = 1


for i in range(1, rows):
    for j in range(1, cols):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print("Total Unique Paths =", dp[rows-1][cols-1])