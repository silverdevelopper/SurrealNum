from ..Surreal_num import * # noktalar dogru da çalışmıyor, ya sys ile ilgili ---şuraya bakın https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
#import Surreal_ num hocam bu da olmuyor
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
    def test_shorten(self):
        x = SurrealShort([Surreal_Converter.convert(2),Surreal_Converter.convert(2)],[Surreal_Converter.convert(5),Surreal_Converter.convert(5)])
        self._check(x == x.shorten,True)
    def test_multiplication(self):
        self._check(Surreal_Converter.convert(2)*Surreal_Converter.convert(5).convert_to_rat()==10,True)
"""
x = Surreal_Converter.convert(1)
y = Surreal_Finite.SurrealThree
x+=5
x.shorten()
print(x.convert_to_rat())
b=Surreal_Finite.SurrealMinusOneHalf+Surreal_Finite.SurrealMinusOne
b.left
print(b.left[0])
"""


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