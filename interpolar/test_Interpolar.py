import interpolar as inter
import unittest


class tester(unittest.TestCase):
    def test_for_point(self):
        A = [[2, 5], [6, 9]]
        x = 4
        right_answer = [x, 7]
        self.assertEqual(inter.interpolar_for_point(A, x), right_answer)

    def test_for_piece_interpolar(self):
        Big_A = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [-1.5, 3, 2, 5, 9]
        right_answer = [[-1.5, -0.5], [3, 4.0], [3, 4.0], [2, 3.0], [5, 5.399999999999999], [9, 11.799999999999999]]
        self.assertEqual(inter.piece_interpolar(Big_A, x), right_answer)

    def test_lagrange_polinom(self):
        Lag_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = 4
        right_answer = [x, 2.12]
        self.assertEqual(inter.lagrange_polimom(Lag_xy, x), right_answer)

if __name__ == '__main__':
    unittest.main()