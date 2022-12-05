from slau import slau
from copy import deepcopy

def fiend_coefficients(A):
    new_A = deepcopy(A)
    b = []
    for i in range(len(new_A)):
        b += [new_A[i][1]]
        new_A[i][1] = 1
    return slau(new_A, b)


def interpolar_for_point(A, x):
    coefficients = fiend_coefficients(A)
    if type(x) in (float, int):
        return [x, coefficients[0] * x + coefficients[-1]]
    elif type(x) == list:
        xy = []
        for point_x in x:
            xy += [[point_x, coefficients[0] * point_x + coefficients[-1]]]
        return xy
    else:
        raise TypeError("x must be int, float or list type")

def piece_interpolar(A, x):
    coefficients = []
    pieces = []
    for i in range(len(A) - 1):
        coefficients += [fiend_coefficients([A[i], A[i+1]])]
        pieces += [[A[i][0], A[i+1][0]]]
    xy = []
    for point in x:
        if point <= pieces[0][0]:
            xy += [[point, point * coefficients[0][0] + coefficients[0][1]]]
        elif point >= pieces[-1][0]:
            xy += [[point, point * coefficients[-1][0] + coefficients[-1][1]]]
        else:
            for i in range(len(pieces)):
                if point >= pieces[i][0] and point <= pieces[i][1]:
                    xy += [[point, point * coefficients[i][0] + coefficients[i][1]]]

    return xy

def set_basis(data_xy, j, x):
    l = 1
    for i in range(len(data_xy)):
        if i != j:
            l *= (x - data_xy[i][0]) / (data_xy[j][0] - data_xy[i][0])
    return l


def lagrange_polimom(data_xy, x):
    L = 0

    for j in range(len(data_xy)):
        L += data_xy[j][1] * set_basis(data_xy, j, x)
    return [x, L]
