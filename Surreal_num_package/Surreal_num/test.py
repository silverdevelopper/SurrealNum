from Surreal_num import *
import unittest

class AdditionTest(unittest.TestCase):
    
    def _check(self, input, expected):
        self.assertEqual(input, expected)

    def test_extend_1(self):
        self._check(1,1)

class MultipicationTest(unittest.TestCase):

    def _check(self, input, expected):
        self.assertEqual(input, expected)
    
    def test_extend_1(self):
        self._check(1,1)
        
class ComperaitonTest(unittest.TestCase):
    
    def _check(self, x, y):
        self.assertEqual(x, y)
    
    def test_sureal_zeros(self):
        self._check(SurrealShort(),Surreal_Finite.SurrealZero)
    
    def test_eq_2_2(self):
        self._check(Surreal_Converter.convert(2), Surreal_Finite.SurrealTwo )
        
    def test_eq_minus_2_2(self):
        self._check(Surreal_Converter.convert(-2), Surreal_Finite.SurrealMinusTwo )
        
    def test_eq_minus_2_1(self):
        self._check(Surreal_Converter.convert(-2) != Surreal_Finite.SurrealMinusOne, True )
        
    def test_le_1(self):
        self._check(Surreal_Converter.convert(1) <= Surreal_Finite.SurrealTwo,True )



if __name__ == '__main__':
    unittest.main()
    a=SurrealShort(left=[Surreal_Finite.SurrealZero])
    b=SurrealShort(left = a,right = 1)
    c=SurrealShort(left= 1,right= b)
   # ComperaitonTest().test_eq_minus_2_1()
    '''print(Surreal_Finite.SurrealOne)
    print( SurrealShort() ==  Surreal_Finite.SurrealOne )
    print( SurrealShort() ==  Surreal_Finite.SurrealThree )
    print( SurrealShort() ==  Surreal_Finite.SurrealZero )'''