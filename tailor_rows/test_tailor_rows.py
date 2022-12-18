import tailor_rows as t_r
import unittest

class tester(unittest.TestCase):
    def test_t_r_exp(self):
        n = 5
        x = 2
        answer = 7.266666666666667
        self.assertEqual(t_r.tailor_exp(n, x), answer)

    def test_t_r_sin(self):
        n = 5
        x = 1.5
        answer = 0.9974949556821353
        self.assertEqual(t_r.tailor_sin(n, x), answer)

    def test_t_r_cos(self):
        n = 5
        x = 5
        answer = -0.16274663800705413
        self.assertEqual(t_r.tailor_cos(n, x), answer)

    def test_t_r_arcsin(self):
        n = 3
        x = 1
        answer = 1.286309523809524
        self.assertEqual(t_r.tailor_arcsin(n, x), answer)

    def test_t_r_arccos(self):
        n = 2
        x = 1
        answer = 0.32912966012822986
        self.assertEqual(t_r.tailor_arccos(n, x), answer)

    def test_error_value_t_r_exp(self):
        n = -1
        with self.assertRaises(ValueError):
            t_r.tailor_exp(n)

    def test_error_value_t_r_sin(self):
        n = -2
        with self.assertRaises(ValueError):
            t_r.tailor_sin(n)

    def test_error_value_t_r_cos(self):
        n = -1
        with self.assertRaises(ValueError):
            t_r.tailor_cos(n)

    def test_error_value_t_r_arcsin(self):
        n = -4
        with self.assertRaises(ValueError):
            t_r.tailor_arcsin(n)

    def test_error_value_t_r_arccos(self):
        n = -8
        with self.assertRaises(ValueError):
            t_r.tailor_arccos(n)

    def test_error_type_t_r_exp(self):
        n = (2, )
        with self.assertRaises(TypeError):
            t_r.tailor_exp(n)

    def test_error_type_t_r_sin(self):
        n = [1]
        with self.assertRaises(TypeError):
            t_r.tailor_sin(n)

    def test_error_type_t_r_cos(self):
        n = "2"
        with self.assertRaises(TypeError):
            t_r.tailor_cos(n)

    def test_error_type_t_r_arcsin(self):
        n = 4.2
        with self.assertRaises(TypeError):
            t_r.tailor_arcsin(n)

    def test_error_type_t_r_arccos(self):
        n = 8.7
        with self.assertRaises(TypeError):
            t_r.tailor_arccos(n)


if __name__ == '__main__':
    unittest.main()