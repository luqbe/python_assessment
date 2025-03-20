import numpy as np
def f_c_r(arr):
    np.set_printoptions(legacy ='1.13')
    floor_arr = np.floor(arr)
    ceil_arr = np.ceil(arr)
    rint_arr = np.rint(arr)
    return f"{floor_arr}\n{ceil_arr}\n{rint_arr}"
