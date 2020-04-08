import unittest

def factorial(n):
    """return n! using recursive solution"""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

class FactorialTest(unittest.TestCase):
    def test_factorial(self) -> None:
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(5),120)

if __name__ == "__main__":
    unittest.main(exit = False)
