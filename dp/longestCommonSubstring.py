a = "pankaj"
b = "jacobpanxxxkaj"


def LCS(i, j):
    if i+1 == len(a) or j+1 == len(b):
        return 1
    if a[i] == b[j]:
        return 1 + LCS(i+1, j+1)
    else:
        return max(LCS(i+1, j), LCS(i, j+1))

print(LCS(0, 0))
