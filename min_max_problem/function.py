import numpy as np
def min_max_2d(arr):
    np_arr = np.array(arr)
    min_values = np.min(np_arr, axis=1)
    return np.max(min_values)


n, m = map(int, input("Enter dimensions (n m): ").split())
arr = [list(map(int, input().split())) for _ in range(n)]

