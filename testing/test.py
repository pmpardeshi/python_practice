import totest
import unittest

class test(unittest.TestCase):
	def test1(self):
		sqrnum=totest.sqr(6)
		self.assertEqual(sqrnum,36)

if __name__ == '__main__':
	unittest.main()