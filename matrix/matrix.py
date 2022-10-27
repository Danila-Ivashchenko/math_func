import vector as v
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
	if ensure_matrix(a, b):
			size_check(a, b)
			for row_id in range(len(a)):
				new_mat += [v.add(a[row_id], b[row_id])]
	else:
		mat, scal = are_mat_num(a, b)
		for row in mat:
			new_mat += [v.add(row, scal)]
	return new_mat

def mul(a, b):
	new_mat = []
	if ensure_matrix(a, b):
			size_for_mul(a, b)
			if (is_matrix(b)):
				for i in range(len(a)):
					buf = []
					for c in range(len(b)):
						cell_buf = 0
						for j in range(len(a[c])):
							cell_buf += a[i][j] * b[j][c]
						buf += [cell_buf]
					new_mat += [buf]
			else:
				for i in range(len(a)):
					for c in range(len(b)):
						cell_buf = 0
						for j in range(len(a[c])):
							cell_buf += a[i][j] * b[j]
					new_mat += [cell_buf]

	else:
		mat, scal = are_mat_num(a, b)
		for row in mat:
			new_mat += [v.mul(row, scal)]

	return new_mat

def mul_row(a, row, scalar = 1):
	is_matrix(a)
	new_mat = deepcopy(a)
	for i in range(len(new_mat[row - 1])):
		new_mat[row][i] *= scalar
	return new_mat

def sub(a, b):
	if ensure_matrix(a, b):
			return add(a, mul(b, -1))
	else:
		mat, scal = are_mat_num(a, b)
		return add(mat, 0 - scal)


def add_rows(a, row1, row2, scalar = 1):
	is_matrix(a)
	new_mat = deepcopy(a)
	new_mat[row1] = v.add(new_mat[row1], v.mul(get_row(new_mat, row2), scalar))
	return new_mat

def sub_rows(a, row1, row2, scalar = 1):
	is_matrix(a)
	new_mat = deepcopy(a)
	new_mat[row1] = v.sub(new_mat[row1], v.mul(get_row(new_mat, row2), scalar))
	return new_mat


def is_matrix(mat):
	if type(mat) != list:
		return False
	elif type(mat) == list:
		if ensure_type_cells(mat):
			return True
	else:
		raise TypeError(f"Must be not list, not {type(mat)}")


def ensure_matrix(mat1, mat2):
	return (is_matrix(mat1) and is_matrix(mat2)) or (is_matrix(mat1) and v.is_vector(mat2))


def ensure_type_cells(mat):
	for row in mat:
		if type(row) == list:
			for cell in row:
				if not (type(cell) in (int, float)):
					mess = f"{cell} is not int or float"
					raise TypeError(mess)
		else:
			return False
	return True


def size_check(mat1, mat2):
	if len(mat1) == len(mat2):
		for row_id in range(len(mat1)):
			if len(mat1[row_id]) != len(mat2[row_id]):
				mess = f"row {row_id} in first matrix len is {mat1[row_id]}, {row_id} in second matrix len is {len(mat2[row_id])}, lens are not similar"
				raise ValueError("Size error")
	else:
		mess = f"first matrix len is {len(mat1)}, second matrix len is {len(mat2)}, lens are not similar"
		raise ValueError(mess)


def size_for_mul(mat1, mat2):
	for row in mat1:
		if len(row) != len(mat2):
			raise ValueError("Size error")


def are_mat_num(mat, num):
	if type(mat) == list:
		if is_matrix(mat) and ensure_type_cells(mat) and type(num) in (int, float):
			return mat, num
	elif type(num) == list:
		if is_matrix(num) and ensure_type_cells(num) and type(mat) in (int, float):
			return num, mat
	else:
		raise TypeError("must be only list or num")