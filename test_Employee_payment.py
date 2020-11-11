import unittest
from Employee_payment import ExecutiveChef 
from Employee_payment import SousChef
from Employee_payment import KitchenManager


class TestExecutiveChef(unittest.TestCase):
    def test_pay(self): 
      
        jack = ExecutiveChef("Jack Clive", 49)
        jack = jack.pay()
      
        self.assertEqual(jack, 'Jack Clive hourly pay is $45')
                         

class TestSousChef(unittest.TestCase):
        def test_pay(self): 
            sarah = SousChef("Sarah Black", 31)
            sarah = sarah.pay()
      
            self.assertEqual(sarah, 'Sarah Black hourly pay is $30')
            
            
            

class TestKitchenManager(unittest.TestCase):
        def test_pay(self): 
            thomas = KitchenManager("Thomas Ford", 28)
            thomas = thomas.pay()
      
            self.assertEqual(thomas, 'Thomas Ford hourly pay is $20')
            
            
if __name__=='__main__':
    unittest.main()          