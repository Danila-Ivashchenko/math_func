import math


def lenght(vec1):
	"""Return length of the vector"""
	is_vector(vec1)
	buf = 0
	for coord in vec1:
		buf += coord * coord
	return math.sqrt(buf)

def scalar(vec1, vec2):
	"""Return scalar product vectors"""
	ensure_vectors(vec1, vec2)
	buf = 0
	for i in range(len(vec1)):
		buf += vec1[i] * vec2[i]
	return buf

def cos(vec1, vec2, delta = 5):
	"""Return cos between two vectors"""
	ensure_vectors(vec1, vec2)
	return scalar(vec1, vec2) / (lenght(vec1) * lenght(vec2))


def is_equal(vec1, vec2, delta = 0):
	"""Check two vectors for equality"""
	ensure_vectors(vec1, vec2)
	for i in range(len(vec1)):
		if abs(vec1[i] - vec2[i]) > delta:
			return False
	return True


def add(vec1, vec2):
	"""Addition float/int constant or vector to the vector"""
	if ensure_vectors(vec1, vec2):
		return [vec1[i] + vec2[i] for i in range(len(vec1))]
	else:
		v, num = vector_and_num(vec1, vec2)
		return [v[i] + num for i in range(len(v))]

def sub(vec1, vec2):
	"""Subtraction float/int constant or vector from the vector"""
	if ensure_vectors(vec1, vec2):
		return [vec1[i] - vec2[i] for i in range(len(vec1))]
	else:
		v, num = vector_and_num(vec1, vec2)
		return [v[i] - num for i in range(len(v))]

def div(vec1, vec2, delta = 3):
	"""Division the vector on float/int constant or vector"""
	if ensure_vectors(vec1, vec2):
		return [vec1[i] / vec2[i] for i in range(len(vec1))]
	else:
		v, num = vector_and_num(vec1, vec2)
		return [v[i] / num for i in range(len(v))]


def mul(vec1, vec2):
	"""Multiplication the vector on float/int constant or vector"""
	if ensure_vectors(vec1, vec2):
		return [(vec1[i] * vec2[i]) for i in range(len(vec1))]
	else:
		v, num = vector_and_num(vec1, vec2)
		return [v[i] * num for i in range(len(v))]


def norm(vec1):
	"""Normalization the vector"""
	is_vector(vec1)
	return div(vec1, lenght(vec1))

def is_colleniar(vec1, vec2, delta = 5):
	"""Check two vectors for colleniar"""
	ensure_vectors(vec1, vec2)
	return abs(cos(vec1, vec2, delta)) == 1.0

def is_one_direction(vec1, vec2, delta = 5):
	"""Check two vectors for the same direction or not"""
	ensure_vectors(vec1, vec2)
	return cos(vec1, vec2, delta) == 1.0

def is_opposite_direction(vec1, vec2, delta = 5):
	"""Check two vectors for opposite direction or not"""
	ensure_vectors(vec1, vec2)
	return cos(vec1, vec2, delta) == -1.0


def is_orthogonal(vec1, vec2, delta = 5):
	"""Check two vectors for orthogonal or not"""
	ensure_vectors(vec1, vec2)
	return cos(vec1, vec2, delta) == 0


def angular(vec1, vec2, delta = 5):
	"""Return angular between two vectors"""
	ensure_vectors(vec1, vec2)
	coss = cos(vec1, vec2, delta)
	rad = math.acos(coss)
	return round(rad / math.pi * 180, 3)

def projection(vec1, vec2):
	"""Return projection of vec2 vector on this vector"""
	ensure_vectors(vec1, vec2)
	return scalar(vec1, vec2) / lenght(vec2)

def change_direction(vec1):
	"""Return vector with opposite direction"""
	is_vector(vec1)
	return tuple(vec1[i] * -1 for i in range(len(vec1)))

def to_str(vec1):
	str = ""
	for i in range(len(vec1) - 1):
		str += f"{vec1[i]}, "
	str += f"{vec1[-1]}"
	return str

def ensure_vectors(v1, v2):
	if type(v1) != list or type(v2) != list:
		return False
	if is_vector(v1) and is_vector(v2):
		ensure_size(v1, v2)
	return True

def is_vector(v):
	if type(v) != list:
		return False
	for item in v:
		if type(item) == list:
			return False
		if type(item) not in (int, float):
			mess = f"Vector must contanin only int or float coordinates, {item} is {type(item)}"
			raise TypeError(mess)
	return True

def ensure_size(v1, v2):
	if len(v1) != len(v2):
		mess = f"first vector len - {len(v1)}, second vector len - {len(v2)}, lens are not similar"
		raise ValueError(mess)
	return True

def vector_and_num(v, num):
	if type(v) == list:
		if is_vector(v) and type(num) in (int, float):
			return v, num
		else:
			mess = f"{num} must be list, int or float type, not {type(num)}"
			raise TypeError(mess)
	elif type(num) == list:
		if is_vector(num) and type(v) in (int, float):
			return num, v
		else:
			mess = f"{v} must be list, int or float type, not {type(v)}"
			raise TypeError(mess)
	else:
		raise TypeError("Arguments don't contain vector, vector must be list type")