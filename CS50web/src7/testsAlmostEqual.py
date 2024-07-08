# https://www.geeksforgeeks.org/python-unittest-assertalmostequal-function/
# https://www.dataquest.io/blog/unit-tests-python/

# test suite 
import unittest 


class TestStringMethods(unittest.TestCase): 
	# negative test function to test if values are almost equal with place 
	def test_negativeWithPlaces(self): 
		first = 4.4555
		second = 4.4566
		decimalPlace = 3
		# error message in case if test case got failed 
		message = "first and second are not almost equal."
		# assert function() to check if values are almost equal 
		self.assertAlmostEqual(first, second, decimalPlace, message) 

	# positive test function to test if values are almost equal with place 
	def test_positiveWithPlaces(self): 
		first = 4.4555
		second = 4.4566
		decimalPlace = 2
		# error message in case if test case got failed 
		message = "first and second are not almost equal."
		# assert function() to check if values are almost equal 
		self.assertAlmostEqual(first, second, decimalPlace, message) 

	# negative test function to test if values are almost equal with delta 
	def test_negativeWithDelta(self): 
		first = 4.4555
		second = 4.4566
		delta = 0.0001
		# error message in case if test case got failed 
		message = "first and second are not almost equal."
		# assert function() to check if values are almost equal 
		self.assertAlmostEqual(first, second, None, message, delta) 

	# positive test function to test if values are almost equal with delta 
	def test_positiveWithDelta(self): 
		first = 4.4555
		second = 4.4566
		delta = 0.002
		# error message in case if test case got failed 
		message = "first and second are not almost equal."
		# assert function() to check if values are almost equal 
		self.assertAlmostEqual(first, second, None, message, delta) 


if __name__ == '__main__': 
	unittest.main() 
