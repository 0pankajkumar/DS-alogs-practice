# Doesn't yield correct results

a = "pankaj"
b = "jacobpanxxxkaj"

cache = [[1]*10]*10

def LCS(i, j):
    if i+1 == len(a) or j+1 == len(b):
        return 1
    if cache[i][j] != 1:
        print("read from cache")
        return cache[i][j]

    if a[i] == b[j]:
        t = LCS(i+1, j+1)
        cache[i][j] = t
        return 1 + t
    else:
        s = LCS(i+1, j)
        t = LCS(i, j+1)
        cache[i+1][j] = s
        cache[i][j+1] = t
        return max(s, t)

print(LCS(0, 0))
print(cache)
