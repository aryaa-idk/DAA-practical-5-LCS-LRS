def lrs(s1, s2):
    m = len(s1)
    n = len(s2)
    c = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif s1[i-1] == s2[j-1] and i != j:
                c[i][j] = 1 + c[i-1][j-1]
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c, c[n][m]

def backtrack_lrs(s1, s2, c):
    m = len(s1)
    n = len(s2)
    lrs_seq = ""

    i = n
    j = m

    while i > 0 and j > 0:
        if c[i][j] == c[i-1][j-1] + 1 and s1[i-1] == s2[j-1] and i != j:
            lrs_seq = s1[i-1] + lrs_seq
            i -= 1
            j -= 1
        elif c[i][j] == c[i-1][j]:
            i -= 1
        else:
            j -= 1
    return lrs_seq

s1 = "AABEBCDD"
s2 = "AABEBCDD"
matrix, result = lrs(s1, s2)
print("The DP matrix:")
for row in matrix:
    print(row)

lrs_sequence = backtrack_lrs(s1, s2, matrix)
print(f"The length of the Longest Repetitive Subsequence is: {result}")
print(f"One of the Longest Repetitive Subsequences is: {lrs_sequence}")
