import unittest
import problem2

class TestProblem2(unittest.TestCase):

	def test_problem2_small(self):
		result = problem2.fibonacci(90)
		self.assertEqual(result, 44)

	def test_problem2_large(self):
		result = problem2.fibonacci(4000000)
		self.assertEqual(result, 4613732)