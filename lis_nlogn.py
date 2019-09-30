inf = 200000000
def get_lis_nlogn(arr):
    I = [inf] * len(arr)
    I[0] = -inf
    lis_len = 0
    for i in range(len(arr)):
        low, high = 0, len(arr)
        while (low <= high):
            mid = (low + high) / 2
            if I[mid] < arr[i]:
                low += 1
            else:
                high = mid - 1
        I[low] = arr[i]
        if lis_len < low:
            lis_len = low
    return lis_len
        

get_lis_nlogn([50, 3, 10, 7, 80, 40])
