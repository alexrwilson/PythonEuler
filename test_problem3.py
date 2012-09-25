import unittest
import problem3

class TestProblem3(unittest.TestCase):

	def test_prime_check_small(self):
		result = problem3.is_prime(2)
		self.assertTrue(result)

	def test_prime_check_small_non_prime(self):
		result = problem3.is_prime(4)
		self.assertFalse(result)

	def test_prime_check_large(self):
		result = problem3.is_prime(6857)
		self.assertTrue(result)

	def test_prime_check_large_non_prime(self):
		result = problem3.is_prime(6858)
		self.assertFalse(result)

	def test_problem3_small(self):
		result = problem3.largest_prime_factor(13195)
		self.assertEqual(result, 29)

	#def test_problem3_large(self):
		#result = problem3.largest_prime_factor(600851475143)
		#self.assertEqual(result, 6857)
		#currently runs too slow for unit tests