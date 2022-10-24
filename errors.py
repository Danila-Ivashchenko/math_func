def is_matrix(mat):
	if type(mat) != list:
		return False
	elif type(mat) == list and ensure_type_cells(mat):
		return True
	else:
		raise TypeError(f"Must be not list, not {type(mat)}")

def ensure_matrix(mat1, mat2):
	return is_matrix(mat1) and is_matrix(mat2)


def ensure_type_cells(mat):
	for row in mat:
		if type(row) == list:
			for cell in row:
				if not(type(cell) in (int, float)):
					mess = f"{cell} is not int or float"
					raise TypeError(mess)
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