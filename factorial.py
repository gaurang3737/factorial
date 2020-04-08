import unittest

def factorial(n):
    """return n! using recursive solution"""
    if n == 1:
        return 1
    else:
        return n * 1

class FactorialTest(unittest.TestCase):
    def test_factorial(self) -> None:
        self.assertEqual(factorial(1),1)

if __name__ == "__main__":
    unittest.main(exit = False)