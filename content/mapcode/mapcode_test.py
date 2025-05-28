# Python
import unittest
from mapcode import loop, limit_map, mapcode

class TestMapcode(unittest.TestCase):
    def test_loop_reaches_fixed_point(self):
        F = lambda x: x // 2
        x = 8
        result = loop(F, x)
        self.assertEqual(result, 0)

    def test_loop_already_fixed_point(self):
        F = lambda x: x
        x = 5
        result = loop(F, x)
        self.assertEqual(result, 5)

    def test_limit_map(self):
        F = lambda x: x // 2
        F_infty = limit_map(F)
        self.assertEqual(F_infty(10), 0)
        self.assertEqual(F_infty(0), 0)

    def test_mapcode_pipeline(self):
        rho = lambda i: i + 1
        F = lambda x: x if x <= 3 else x - 1
        pi = lambda x: x * 2
        f = mapcode(rho, F, pi)
        self.assertEqual(f(5), 6)  # rho(5)=6, F: 6->5->4->3, pi(3)=6
        self.assertEqual(f(1), 4)  # rho(1)=2, F: 2, pi(2)=4

if __name__ == '__main__':
    unittest.main()