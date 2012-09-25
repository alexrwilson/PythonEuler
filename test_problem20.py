import unittest
import problem20

class TestProblem20(unittest.TestCase):

	def test_small_factorial(self):
		result = problem20.factorial(10)
		self.assertEqual(result, 3628800)

	def test_large_factorial(self):
		result = problem20.factorial(100)
		self.assertEqual(result / int(1e155), 933L) 
		#approximate comparison due to not wanting to type out massive numbers!

	def test_small_sum_digits(self):
		result = problem20.sum_digits(405)
		self.assertEqual(result, 9)

	def test_large_sum_digits(self):
		result = problem20.sum_digits(int(10101010222110))
		self.assertEqual(result, 12)

	def test_problem20_small(self):
		result = problem20.sum_factorial_digits(10)
		self.assertEqual(result, 27)

	def test_problem20_large(self):
		result = problem20.sum_factorial_digits(100)
		self.assertEqual(result, 648)

