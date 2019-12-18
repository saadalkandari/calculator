import io
from contextlib import redirect_stdout
from unittest.mock import patch
import unittest
import calculator


class ContainersTestCase(unittest.TestCase):

	def setUp(self):
		self.response = io.StringIO()

	def test_mult(self):
		user_input = ['4', '5', '*']
		
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				calculator.main()		 
		self.assertTrue( '20' in self.response.getvalue())

	def test_add(self):
		user_input = ['4', '5', '+']
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				calculator.main()     
		self.assertTrue( '9' in self.response.getvalue())

	def test_div(self):
		user_input = ['10', '2', '/']
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				calculator.main()
			 
		self.assertTrue( '5' in self.response.getvalue())

	def test_sub(self):
		user_input = ['5', '4', '-']
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				calculator.main()
			
		self.assertTrue( '1' in self.response.getvalue())

	def test_not_number(self):
		user_input = ['5', 'a', '-']
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				calculator.main()
			
		self.assertFalse(self.response.getvalue()=='')

	def test_invalid_operation(self):
		user_input = ['5', '4', 'v']
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				calculator.main()
		
		value = self.response.getvalue()
		self.assertFalse('1' in value)
		self.assertFalse('9' in value)
		self.assertFalse('20' in value)




if __name__ == '__main__':
	unittest.main()




