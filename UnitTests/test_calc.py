import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_divide(self):  # must start with 'test'
        result = calc.divide1(3, 4)
        self.assertEqual(result, .75)
        # self.assertRaises(ValueError, calc.divide1, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide1(1, 0)

    # def test_divide2(self):  # divide 2 is a print function that doesn't return anything
    #     result = calc.divide2(3, 4)
    #     self.assertEqual(result, .75)

    def test_power_recur(self):
        self.assertEqual(calc.power_recur(12, 0), 1)
        self.assertEqual(calc.power_recur(3, -4), 1 / 81)
        self.assertEqual(calc.power_recur(0, -2), 0)
        self.assertEqual(calc.power_recur(-2, 2), 4)
        self.assertEqual(calc.power_recur(-2, 3), -8)
        self.assertEqual(calc.power_iter(-3, -2), 1 / 9)
        self.assertEqual(calc.power_iter(-4, -1), (-1 / 4))

    def test_power_recur2(self):
        self.assertEqual(calc.power_recur2(14, 3), 2744)
        self.assertEqual(calc.power_recur2(3, -3), 1 / 27)
        self.assertEqual(calc.power_recur2(0, 22), 0)
        self.assertEqual(calc.power_recur2(-2, 0), 1)
        self.assertEqual(calc.power_iter(-3, -2), 1 / 9)
        self.assertEqual(calc.power_iter(-4, -1), (-1 / 4))


    def test_power_iter1(self):
        self.assertEqual(calc.power_iter(6, 4), 1296)
        self.assertEqual(calc.power_iter(9, -2), 1 / 81)
        self.assertEqual(calc.power_iter(0, -2), 0)
        self.assertEqual(calc.power_iter(-3, -2), 1/9)
        self.assertEqual(calc.power_iter(-4, -1), (-1/4))



if __name__ == '__main__':
    unittest.main()