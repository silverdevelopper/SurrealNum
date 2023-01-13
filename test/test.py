from Surreal_num_package.Surreal_num import SurrealShort
import unittest

'''
Tests check several rewriting rules for the logical optimization
of relational algebra expressions.

Tests assume that all relational algebra queries have been
compiled from SQL queries by the canonical translation.
Therefore, they use projection, selection, the cross product
and the renaming operator only.
'''

'''
Tests that selections are broken up correctly.
'''

class AdditionTest(unittest.TestCase):
    
    def _check(self, input, expected):
        self.assertEqual(input, expected)

    def test_extend_1(self):
        self._check("\select_{Person.gender = 'f' and Person.age = 16 and Person.name = 'Amy'} Person;",
                    "\select_{Person.gender = 'f'} \select_{Person.age = 16} \select_{Person.name = 'Amy'} Person;")

class MultipicationTest(unittest.TestCase):

    def _check(self, input, expected):
        self.assertEqual(input, expected)

    def test_extend_1(self):
        self._check("\project_{E.pizza} (\select_{E.pizza = 'mushroom'} ((\\rename_{E: *} Eats) \cross Frequents));",
                    "\project_{E.pizza} ((\select_{E.pizza = 'mushroom'} \\rename_{E: *}(Eats)) \cross Frequents);")

    def test_extend_2(self):
        self._check("\select_{E.pizza = 'mushroom'} ((\\rename_{E: *} Eats) \cross Frequents);",
                    "(\select_{E.pizza = 'mushroom'} \\rename_{E: *}(Eats)) \cross Frequents;")



if __name__ == '__main__':
    unittest.main()
