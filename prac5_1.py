X=input("Enter the first sequence: ")
Y=input("Enter the second sequence: ")

m = len(X)
n = len(Y)

if m == 0 or n == 0:
    print("Empty strings")
else:
    cost_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    direction_matrix = [[''] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        cost_matrix[i][0] = 0
        direction_matrix[i][0] = 'u'
    for j in range(n + 1):
        cost_matrix[0][j] = 0
        direction_matrix[0][j] = 's' 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                cost_matrix[i][j] = cost_matrix[i - 1][j - 1] + 1
                direction_matrix[i][j] = 'd'  
            elif cost_matrix[i - 1][j] >= cost_matrix[i][j - 1]:
                cost_matrix[i][j] = cost_matrix[i - 1][j]
                direction_matrix[i][j] = 'u' 
            else:
                cost_matrix[i][j] = cost_matrix[i][j - 1]
                direction_matrix[i][j] = 's' 
    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if direction_matrix[i][j] == 'd':
            lcs = X[i - 1] + lcs
            i -= 1
            j -= 1
        elif direction_matrix[i][j] == 'u':
            i -= 1
        else:
            j -= 1

    print("Cost Matrix:")
    for row in cost_matrix:
        print(row)
    print("Direction Matrix:")
    for row in direction_matrix:
        print(row)
    print("Final Cost of LCS:", cost_matrix[m][n])
    print("LCS:", lcs)
