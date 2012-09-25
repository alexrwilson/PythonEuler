import unittest
import problem4

class TestProblem4(unittest.TestCase):

	def test_small_palindrome(self):
		result = problem4.is_palindrome(404)
		self.assertTrue(result)

	def test_small_non_palindrome(self):
		result = problem4.is_palindrome(405)
		self.assertFalse(result)

	def test_large_palindrome(self):
		result = problem4.is_palindrome(906609)
		self.assertTrue(result)

	def test_large_non_palindrome(self):
		result = problem4.is_palindrome(916511)
		self.assertFalse(result)

	def test_problem4_small(self):
		result = problem4.get_palindrome(99)
		self.assertEqual(result, 9009)

	#def test_problem4_small(self):
	#	result = problem4.get_palindrome(999)
	#	self.assertEqual(result, 906609)
	#Runs too slow for unit test