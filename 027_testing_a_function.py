import unittest
from location_name import get_location_name

class NameTestCase(unittest.TestCase):
    def test_location_name(self):
        location = get_location_name('santiago','chile')
        self.assertEqual(location, 'Santiago, Chile')
    
    def test_location_name_and_population(self):
        location_and_population = get_location_name('santiago', 'chile', '500000')
        self.assertEqual(location_and_population, "Santiago, Chile- 500000") 
        
    
if __name__ == '__main__':
    unittest.main()
    