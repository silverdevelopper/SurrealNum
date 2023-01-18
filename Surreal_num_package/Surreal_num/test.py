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
        self._check(SurrealShort(),S_F.SurrealZero)
    
    def test_eq_2_2(self):
        self._check(Surreal_Converter.convert(2), S_F.SurrealTwo )
        
    def test_eq_minus_2_2(self):
        self._check(Surreal_Converter.convert(-2), S_F.SurrealMinusTwo )
        
    def test_eq_minus_2_1(self):
        self._check(Surreal_Converter.convert(-2) != S_F.SurrealMinusOne, True )
        
    def test_le_1(self):
        self._check(Surreal_Converter.convert(1) <= S_F.SurrealTwo,True )



if __name__ == '__main__':
    unittest.main()
    a=SurrealShort(left=[S_F.SurrealZero])
    b=SurrealShort(left = a,right = 1)
    c=SurrealShort(left= 1,right= b)
   # ComperaitonTest().test_eq_minus_2_1()
    '''print(S_F.SurrealOne)
    print( SurrealShort() ==  S_F.SurrealOne )
    print( SurrealShort() ==  S_F.SurrealThree )
    print( SurrealShort() ==  S_F.SurrealZero )'''