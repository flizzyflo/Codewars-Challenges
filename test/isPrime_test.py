
import unittest
from isPrime import isPrime

class TestPrimeNumbers(unittest.TestCase):

    def test_isPrime(self):
        self.assertEqual(isPrime(7), True)
        self.assertEqual(isPrime(11), True)
        self.assertEqual(isPrime(29), True)
        self.assertEqual(isPrime(31), True)
        self.assertEqual(isPrime(43), True)
        self.assertEqual(isPrime(53), True)
        self.assertEqual(isPrime(97), True)
        self.assertEqual(isPrime(89), True)

    
    def test_noPrime(self):
        self.assertEqual(isPrime(4), False)
        self.assertEqual(isPrime(10), False)
        self.assertEqual(isPrime(125), False)
        self.assertEqual(isPrime(4306), False)


    def test_wrongInput(self):
        self.assertEqual(isPrime("5"), False)
        self.assertEqual(isPrime(5.0), False)
        self.assertEqual(isPrime(""), False)

if __name__ == "__main__":
    unittest.main()