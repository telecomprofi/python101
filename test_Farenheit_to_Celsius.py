import unittest
from Farenheit_to_Celsius import to_celsius
#from math import pi

class TestFarenheitToCelsius(unittest.TestCase):
  def testCelsius(self):
    # Test temperature when Farenheits >=0
    self.assertAlmostEqual(to_celsius(1), -17.22222222222222)
    self.assertAlmostEqual(to_celsius(0), -17.77777777777778)
    self.assertAlmostEqual(to_celsius(32), 0)
  def test_values(self):
    # Make sure value errors are raised when necessary
    self.assertRaises(ValueError, to_celsius, -2)
  def test_types(self):
    # Make sure type erros are raised when Temperature are not real number
    self.assertRaises(TypeError, to_celsius, 3+5j)
    self.assertRaises(TypeError, to_celsius, True)
    self.assertRaises(TypeError, to_celsius, "temperature") 
