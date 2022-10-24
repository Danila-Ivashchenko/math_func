import vector as v
import unittest


class  tester(unittest.TestCase):

	def test_add_equal_1(self):
		a = [1, 2, 3, 0]
		answer = [2, 3, 4, 1]
		self.assertEqual(v.add(a, 1), answer)

	def test_add_equal_2(self):
		a = [1, 2, 3, 0]
		answer = [2.5, 3.5, 4.5, 1.5]
		self.assertEqual(v.add(a, 1.5), answer)

	def test_add_equal_3(self):
		a = [1, 2, 3, 0]
		c = [99, 12.3, 33.12, -12.333]
		answer = [100, 14.3, 36.12, -12.333]
		self.assertEqual(v.add(a, c), answer)

	def test_add_errors(self):
		a = [1, 2, 3]
		wrong_v1 = ['1', 2, 3, 0]
		wrong_v2 = [True, 2, 3, 0]
		wrong_v3 = [[1, 2], [3, 4]]
		wrong_v4 = [1, 2, 3, 0, 12]

		with self.assertRaises(TypeError):
			v.add(a, wrong_v1)
		with self.assertRaises(TypeError):
			v.add(a, wrong_v2)
		with self.assertRaises(TypeError):
			v.add(a, wrong_v3)
		with self.assertRaises(TypeError):
			v.add(a, '12')
		with self.assertRaises(ValueError):
			v.add(a, wrong_v4)
	
	def test_sub_equal_1(self):
		a = [1, 2, 3, 0]
		answer = [0, 1, 2, -1]
		self.assertEqual(v.sub(a, 1), answer)

	def test_sub_equal_2(self):
		a = [1, 2, 3, 0]
		answer = [-0.5, 0.5, 1.5, -1.5]
		self.assertEqual(v.sub(a, 1.5), answer)

	def test_sub_equal_3(self):
		a = [1, 2, 3, 0]
		c = [99, 12.3, 33.1, -12.333]
		answer = [-98, -10.3, -30.1, 12.333]
		self.assertEqual(v.sub(a, c), answer)

	def test_sub_errors(self):
		a = [1, 2, 3, 4]
		wrong_v1 = ['1', 2, 3, 0]
		wrong_v2 = [True, 2, 3, 0]
		wrong_v3 = [[1, 2], [3, 4]]
		wrong_v4 = [1, 2, 3, 0, 12]

		with self.assertRaises(TypeError):
			v.sub(a, wrong_v1)
		with self.assertRaises(TypeError):
			v.sub(a, wrong_v2)
		with self.assertRaises(TypeError):
			v.sub(a, wrong_v3)
		with self.assertRaises(TypeError):
			v.sub(a, '12')
		with self.assertRaises(ValueError):
			v.sub(a, wrong_v4)

	def test_mul_equal_1(self):
		a = [1, 2, 3, 0]
		answer = [2, 4, 6, 0]
		self.assertEqual(v.mul(a, 2), answer)

	def test_mul_equal_2(self):
		a = [1, 2, 3, 0]
		answer = [2.5, 5, 7.5, 0]
		self.assertEqual(v.mul(a, 2.5), answer)

	def test_mul_equal_3(self):
		a = [1, 2, 3, 0]
		c = [99.11, 12.3, 33, -12.333]
		answer = [99.11, 24.6, 99, 0]
		self.assertEqual(v.mul(a, c), answer)

	def test_mul_errors(self):
		a = [1, 2, 3, 0]

		wrong_v1 = ['1', 2, 3, 0]
		wrong_v2 = [True, 2, 3, 0]
		wrong_v3 = [[1, 2], [3, 4]]
		wrong_v4 = [1, 2, 3, 0, 12]

		with self.assertRaises(TypeError):
			v.mul(a, wrong_v1)
		with self.assertRaises(TypeError):
			v.mul(a, wrong_v2)
		with self.assertRaises(TypeError):
			v.mul(a, wrong_v3)
		with self.assertRaises(TypeError):
			v.mul(a, '12')
		with self.assertRaises(ValueError):
			v.mul(a, wrong_v4)
	
	def test_div_equal_1(self):
		a = [33, 22, 44, 101]
		answer = [16.5, 11, 22, 50.5]
		self.assertEqual(v.div(a, 2), answer)

	def test_div_equal_2(self):
		a = [33, 22, 44, 101]
		answer = [13.2, 8.8, 17.6, 40.4]
		self.assertEqual(v.div(a, 2.5), answer)

	def test_div_equal_3(self):
		a = [33, 22, 44, 101]
		c = [3, 11, 8, 1]
		answer = [11, 2, 5.5, 101]
		self.assertEqual(v.div(a, c), answer)

	def test_div(self):
		a = [33, 22, 44, 101]
		wrong_v1 = ['1', 2, 3, 0]
		wrong_v2 = [True, 2, 3, 0]
		wrong_v3 = [[1, 2], [3, 4]]
		wrong_v4 = [1, 2, 3, 0, 12]

		with self.assertRaises(TypeError):
			v.div(a, wrong_v1)
		with self.assertRaises(TypeError):
			v.div(a, wrong_v2)
		with self.assertRaises(TypeError):
			v.div(a, wrong_v3)
		with self.assertRaises(TypeError):
			v.div(a, '12')
		with self.assertRaises(ValueError):
			v.div(a, wrong_v4)

	def test_cos_equeal_1(self):
		a_1 = [1, 0, 0]
		b_1 = [0, 1, 1]
		self.assertEqual(v.cos(a_1, b_1) , 0)

	def test_cos_equeal_2(self):
		a_2 = [3, 4]
		b_2 = [4, 3]
		self.assertEqual(v.cos(a_2, b_2), 0.96)

	def test_cos_equeal_3(self):
		a_3 = [3, 4, 0]
		b_3 = [4, 4, 2]
		self.assertEqual(v.cos(a_3, b_3), 14/15)

	def test_cos_errors(self):
		a = [1, 2]
		b = [1, 2, 3]
		with self.assertRaises(TypeError):
			v.cos(a, 2)
		with self.assertRaises(ValueError):
			v.cos(a, b)
	
	def test_scalar_equeal_1(self):
		a = [5, -4]
		b = [2, 1]
		self.assertEqual(v.scalar(a, b), 6)

	def test_scalar_equeal_2(self):
		a = [0, 3]
		b = [7, -1]
		self.assertEqual(v.scalar(a, b), -3)

	def test_scalar_equeal_3(self):
		a = [5, 2]
		b = [4, -1]
		self.assertEqual(v.scalar(a, b), 18)

	def test_scalar_errors(self):
		a = [1, 2]
		b = ['1', 2]
		c = [1, 2, 3]

		with self.assertRaises(TypeError):
			v.scalar(a, b)
		with self.assertRaises(ValueError):
			v.scalar(a, c)

if __name__ == '__main__':
    unittest.main()