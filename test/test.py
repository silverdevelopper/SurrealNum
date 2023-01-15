from Surreal_num import *
import unittest

class AdditionTest(unittest.TestCase):
    
    def _check(self, input, expected):
        self.assertEqual(input, expected)

    def test_extend_1(self):
        self._check(None,None)

class MultipicationTest(unittest.TestCase):

    def _check(self, input, expected):
        self.assertEqual(input, expected)
    
    def test_extend_1(self):
        self._check(None,None)
        
class ComperaitonTest(unittest.TestCase):
    
    def _check(self, x, y):
        self.assertEqual(x, y)
    
    def test_sureal_zeros(self):
        self._check(SurrealShort(),Surreal_Finite.SurrealZero)
    
    def test_eq(self):
        self._check(None,None)
  
class ComperaitonTest(unittest.TestCase):
    def _check(self, x, y):
        self.assertEqual(x <= y, True)
              
    def test_sureal_le(self):
        self._check(SurrealShort(),Surreal_Finite.SurrealZero)
        
    def test_two_surreals(self):
        self._check(None,None)



if __name__ == '__main__':
    unittest.main()

a=SurrealShort(left=[Surreal_Finite.SurrealZero])
b=SurrealShort(left = a,right = None)
c=SurrealShort(left= None,right= b)

print(Surreal_Finite.SurrealOne)
print( SurrealShort() ==  Surreal_Finite.SurrealOne )
print( SurrealShort() ==  Surreal_Finite.SurrealThree )
print( SurrealShort() ==  Surreal_Finite.SurrealZero )
#print( Surreal_Converter.convert(2) ==  Surreal_Finite.SurrealTwo )