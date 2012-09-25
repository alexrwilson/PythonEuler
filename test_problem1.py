import unittest
import problem1

class TestProblem1(unittest.TestCase):

	def test_problem1_small(self):
		result = problem1.get_sum(10)
		self.assertEqual(result, 23)

	def test_problem1_large(self):
		result = problem1.get_sum(1000)
		self.assertEqual(result, 233168)