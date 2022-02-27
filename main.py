import numpy as np


def rank_of_array(test):
    num = np.ndim(test)
    return num
x = np.array([1, 2, 3])
y = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(rank_of_array(x))
print(rank_of_array(y))
