import unittest
from example_package import example

class TestExample(unittest.TestCase):

    def setUp(self):
        self.temp = 32
    
    def test_fahrToKelv(self):
        '''
        make sure freezing is calculated correctly
        '''
        self.assertAlmostEqual(example.fahrToKelv(self.temp),273.15,2)
        
#        assert example.fahrToKelv(32) == 273.15, 'incorrect freezing point!'

if __name__ == '__main__':
    unittest.main()
