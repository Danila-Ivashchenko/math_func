from slau import *

A = [[2, 5], [6, 9]]
data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]

def find_line_function(A):
    new_A = deepcopy(A)
    b = []
    for i in range(len(new_A)):
        b += [new_A[i][1]]
        new_A[i][1] = 1

    return slau(new_A, b)


def interpolar(A, x):
    func_coefs = find_line_function(A)
    a, k = func_coefs[0], func_coefs[1]
    return a * x + k

def big_interpolar(data_xy, xy):
    func_coefs = []
    for i in range(len(data_xy) - 1):
        func_coefs += [find_line_function([data_xy[i], data_xy[i + 1]])]

    print(func_coefs)
