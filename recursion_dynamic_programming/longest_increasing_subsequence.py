
def LIS_brute(arr):
    longestList = list()
    for i in range(len(arr)):
        if i < len(arr):
            t = [arr[i]]
        else:
            continue
        for j in range(i+1, len(arr)):
            if t[-1] < arr[j]:
                t.append(arr[j])
        longestList.append(t)
    ans = list()
    for l in longestList:
        if len(l) > len(ans):
            ans = l
    print(longestList)
    # O(n^2) time complexity
    # O(k*n) space complexity

# def LIS_recursive():
#     ss


arr = [1,2,3,4,5,6]
LIS_brute(arr)
