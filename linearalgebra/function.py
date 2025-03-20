import numpy as np
def determinant(arr):
    np_arr=np.array(arr)
    determinant=np.linalg.det(np_arr)
    return round(determinant,1)