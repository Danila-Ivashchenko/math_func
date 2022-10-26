import vector as v
import errors as e
from copy import deepcopy

def transponir(a):
	return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

def get_row(a, row_id):
	return a[row_id]

def get_coll(a, coll_id):
	return get_row(transponir(a), coll_id)

def change_rows(a, row1, row2, do_copy = False):
	if (do_copy):
		new_mat = deepcopy(a)
		buf = get_row(new_mat, row2)
		new_mat[row2] = new_mat[row1]
		new_mat[row1] = buf
		return new_mat
	else:
		buf = get_row(a, row2)
		a[row2] = a[row1]
		a[row1] = buf

def add(a, b):
	new_mat = []
	if e.ensure_matrix(a, b):
			e.size_check(a, b)
			for row_id in range(len(a)):
				new_mat += [v.add(a[row_id], b[row_id])]
	else:
		mat, scal = e.are_mat_num(a, b)
		for row in mat:
			new_mat += [v.add(row, scal)]
	return new_mat

def mul(a, b):
	new_mat = []
	if e.ensure_matrix(a, b):
			e.size_for_mul(a, b)
			for i in range(len(a)):
				buf = []
				for c in range(len(b)):
					cell_buf = 0
					for j in range(len(a[c])):
						cell_buf += a[i][j] * b[j][c]	
					buf += [cell_buf]
				new_mat += [buf]
	else:
		mat, scal = e.are_mat_num(a, b)
		for row in mat:
			new_mat += [v.mul(row, scal)]

	return new_mat

def mul_row(a, row, scalar = 1):
	e.is_matrix(a)
	new_mat = deepcopy(a)
	for i in range(len(new_mat[row - 1])):
		new_mat[row][i] *= scalar
	return new_mat

def sub(a, b):
	if e.ensure_matrix(a, b):
			return add(a, mul(b, -1))
	else:
		mat, scal = e.are_mat_num(a, b)
		return add(mat, 0 - scal)


def add_rows(a, row1, row2, scalar = 1):
	e.is_matrix(a)
	new_mat = deepcopy(a)
	new_mat[row1] = v.add(new_mat[row1], v.mul(get_row(new_mat, row2), scalar))
	return new_mat

def sub_rows(a, row1, row2, scalar = 1):
	e.is_matrix(a)
	new_mat = deepcopy(a)
	new_mat[row1] = v.sub(new_mat[row1], v.mul(get_row(new_mat, row2), scalar))
	return new_mat