def get_lis(arr):
    lis = [1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)
    
get_lis([50, 3, 10, 7, 80, 40])
