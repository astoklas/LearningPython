import unittest

class TestStringMethods(unittest.TestCase):

  def runTest(self):
      self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()