import matrix as m
import vector as v
from copy import deepcopy

def ensure_mat_slau(mat, keys):
    if type(mat) != list:
        raise TypeError("Matrix with coefficients must be list type")
    for row in mat:
        if type(row) != list:
            mess = f"Matrix with coefficients must consist lists not {type(row)}"
            raise TypeError(mess)
        if len(row) != len(mat):
            mess = f"Matrix must be square, row's len ({len(row)}) is not equael matrix's len ({len(mat)})"
            raise ValueError(mess)
        for cell in row:
            if not(type(cell) in (int, float)):
                mess = f"Coefficients must be int or float, {cell} is not {type(cell)}"
                raise TypeError(mess)
    if type(keys) != list:
        raise TypeError("Matrix with scalars must be list type")
    for cell in keys:
        if not (type(cell) in (int, float)):
            mess = f"Keys must be int or float, {cell} is not {type(cell)}"
            raise TypeError(mess)
    if len(mat) != len(keys):
        mess = f"sizes matrix with coefficients and matrix with scalars must be similar"
        raise ValueError(mess)

def slau(mat, keys):
    ensure_mat_slau(mat, keys)

    new_mat = deepcopy(mat)
    new_keys = deepcopy(keys)
    shake_matrix_rows(new_mat, new_keys)

    #print(new_mat, '\t', new_keys)
    new_mat, new_keys = forward_sub(new_mat, new_keys)
    new_mat, new_keys = back_sub(new_mat, new_keys)

    #print(new_mat)
    return new_keys

def forward_sub(mat, keys):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j > i:
                break
            if i != j:
                if mat[i][j] != 0:
                    if mat[j][j] == 0:
                        m.change_rows(mat, i, j)
                        buf = keys[j]
                        keys[j] = keys[i]
                        keys[i] = buf
                    keys[i] -= keys[j] * mat[i][j]
                    mat = m.sub_rows(mat, i, j, mat[i][j])
                    #print('f' ,mat,'\t', keys)
            else:
                if mat[i][i] == 0:
                    continue
                elif mat[i][i] != 1:
                    keys[i] /= mat[i][i]
                    mat = m.mul_row(mat, i, 1 / mat[i][i])
    return mat, keys

def back_sub(mat, keys):
     for i in range(len(mat) - 1, -1, -1):
         for j in range(len(mat) - 1, -1, -1):
             if i != j:
                 if mat[i][j] != 0:
                     keys[i] -= keys[j] * mat[i][j]
                     mat = m.sub_rows(mat, i, j, mat[i][j])
                     #print('b', mat,'\t', keys)
             else:
                 if mat[i][i] == 0:
                     raise ValueError("invalid matrix")
                 if mat[i][i] != 1:
                     keys[i] /= mat[i][i]
                     mat = m.mul_row(mat, i, 1 / mat[i][i])
     return mat, keys


def shake_matrix_rows(mat, keys):
    for i in range(len(mat)):
        if mat[i][i] == 0:
            changed = False
            for j in range(len(mat)):
                if mat[j][i] != 0 and mat[i][j] != 0:
                    m.change_rows(mat, i, j)
                    buf = keys[i]
                    keys[j] = keys[i]
                    keys[i] = buf
                    changed = True
                    break
            if not(changed):
                mess = f"invalid matrix, {mat[i][i]} has zero on pos {i}, {i}."
                raise ValueError(mess)