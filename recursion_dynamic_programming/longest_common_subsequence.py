# Classic Algorithm
# Find longest common subsequence between two strings

def LCS(i, j):
    if (i+1 == len(s1)) or (j+1 == len(s2)):
        return 1
    elif s1[i] != s2[j]:
        return max(LCS(i, j+1), LCS(i+1, j))
    else:
        return 1 + LCS(i+1, j+1)



s1 = "abcdefg"
s2 = "xybzdfzg"
ans = LCS(0, 0)
print(ans)
