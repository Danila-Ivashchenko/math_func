import matrix as mat
from random import randint
import unittest

class  tester(unittest.TestCase):

	"""Tests add"""
	def test_add_value_scalar(self):
		a = [[2, 3], [5, 3], [2, 3]]
		scalar = 3
		answer = [[5, 6], [8, 6], [5, 6]]
		self.assertEqual(mat.add(a, scalar), answer)

	def test_add_value_mat(self):
		a = [[2, 3], [5, 3], [2, 3]]
		b = [[7, 3], [3, 6], [55, 42]]
		answer = [[9, 6], [8, 9], [57, 45]]
		self.assertEqual(mat.add(a, b), answer)

	def test_add_values_mat_valueError(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_1 = [[5, 6], [8, 6]]
		with self.assertRaises(ValueError):
			mat.add(a, wrong_mat_1)

	def test_add_values_scalar_typeError(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_scalar = "3"
		with self.assertRaises(TypeError):
			mat.add(a, wrong_scalar)

	def test_add_values_scalar_typeError_1(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_2 = [[5, 6], [8, 6], ["3", 3]]
		with self.assertRaises(TypeError):
			mat.add(a, wrong_mat_2)

	def test_add_values_scalar_typeError_2(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_3 = [[5, 6], [8, 6], "23"]
		with self.assertRaises(TypeError):
			mat.add(a, wrong_mat_3)

	"""Tests mul"""
	def test_mul_value_scalar(self):
		a = [[2, 3], [5, 3], [2, 3]]
		scalar = 3
		answer = [[6, 9], [15, 9], [6, 9]]
		self.assertEqual(mat.mul(a, scalar), answer)

	def test_mul_value_mat(self):
		a = [[2, 3], [5, 3], [2, 3]]
		scalar = [[7, 3, 5], [3, 6, 4]]
		answer = [[23, 24], [44, 33], [23, 24]]
		self.assertEqual(mat.mul(a, scalar), answer)

	def test_div_value_scalar(self):
		a = [[2, 3], [5, 3], [2, 3]]
		scalar = 1/2
		answer = [[1.0, 1.5], [2.5, 1.5], [1.0, 1.5]]
		self.assertEqual(mat.mul(a, scalar), answer)

	def test_mul_values_mat_valueError(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_1 = [[5, 6], [8, 6], [23, 11]]
		with self.assertRaises(ValueError):
			mat.mul(a, wrong_mat_1)

	def test_mul_values_scalar_typeError(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_scalar = "3"
		with self.assertRaises(TypeError):
			mat.mul(a, wrong_scalar)

	def test_mul_values_scalar_typeError_1(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_2 = [[5, 6], ["3", 3]]
		with self.assertRaises(TypeError):
			mat.mul(a, wrong_mat_2)

	def test_mul_values_scalar_typeError_2(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_3 = [[5, 6], "23"]
		with self.assertRaises(TypeError):
			mat.mul(a, wrong_mat_3)

	"""Tests sub"""
	def test_sub_value_scalar(self):
		a = [[2, 3], [5, 3], [2, 3]]
		scalar = 3
		answer = [[-1, 0], [2, 0], [-1, 0]]
		self.assertEqual(mat.sub(a, scalar), answer)

	def test_sub_value_mat(self):
		a = [[2, 3], [5, 3], [2, 3]]
		b = [[7, 3], [3, 6], [55, 42]]
		answer = [[-5, 0], [2, -3], [-53, -39]]
		self.assertEqual(mat.sub(a, b), answer)

	def test_sub_values_mat_valueError(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_1 = [[5, 6], [8, 6], [23, 11]]
		with self.assertRaises(ValueError):
			mat.mul(a, wrong_mat_1)

	def test_sub_values_scalar_typeError(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_scalar = "3"
		with self.assertRaises(TypeError):
			mat.mul(a, wrong_scalar)

	def test_sub_values_scalar_typeError_1(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_2 = [[5, 6], ["3", 3]]
		with self.assertRaises(TypeError):
			mat.mul(a, wrong_mat_2)

	def test_sub_values_scalar_typeError_2(self):
		a = [[2, 3], [5, 3], [2, 3]]
		wrong_mat_3 = [[5, 6], "23"]
		with self.assertRaises(TypeError):
			mat.mul(a, wrong_mat_3)

	"""Tests rows operations"""
	def test_add_value_rows(self):
		a = [[2, 3], [5, 3], [2, 3]]
		scalar = 2
		id_1 = 0
		id_2 = 1
		answer = [[12, 9], [5, 3], [2, 3]]
		self.assertEqual(mat.add_rows(a, id_1, id_2, scalar), answer)

	def test_add_value_rows(self):
		a = [[2, 3], [5, 3], [2, 3]]
		a_primal = [[2, 3], [5, 3], [2, 3]]
		scalar = 2
		id_1 = 0
		id_2 = 1
		answer = [[12, 9], [5, 3], [2, 3]]
		self.assertEqual(mat.add_rows(a, id_1, id_2, scalar), answer)
		self.assertEqual(a, a_primal)

	def test_mul_value_rows(self):
		a = [[2, 3], [5, 3], [2, 3]]
		a_primal = [[2, 3], [5, 3], [2, 3]]
		scalar = 2
		id = 0
		answer = [[4, 6], [5, 3], [2, 3]]
		self.assertEqual(mat.mul_row(a, id,scalar), answer)
		self.assertEqual(a, a_primal)

	def test_change_value_rows(self):
		a = [[2, 3], [5, 3], [2, 3]]
		a_primal = [[2, 3], [5, 3], [2, 3]]
		id_1 = 0
		id_2 = 1
		answer = [[5, 3], [2, 3], [2, 3]]
		self.assertEqual(mat.change_rows(a, id_1, id_2, True), answer)
		self.assertEqual(a, a_primal)
		mat.change_rows(a, id_1, id_2)
		self.assertEqual(a, answer)


if __name__ == '__main__':
    unittest.main()