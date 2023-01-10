from .Surreal_num_utils import *
from typing import List,Set
class Ordinal:
    def __init__(self, number:int = None):
        if number:
            self.value = number
        else:
            self.value = Zero
            
    def __str__(self) -> str:
        return str(self.value)
            

class Zero(Ordinal):
    def __init__(self):
        pass
    def __str__(self) -> str:
        return "Ø"
    
class SurrealShort(object):
    calculated_surreals = {}
    count = 10000
    def __init__(self, left: Set['SurrealShort'] = None, right:Set['SurrealShort' ]= None):
        self.left:Set[SurrealShort]  = left if left else set()
        self.right:Set[SurrealShort] = right if right else set()
        self.ordinal: Ordinal = SurrealShort.calculate_ordinal(self)
        self.is_valid(self)
        self.h = hash(str(SurrealShort.count))
        SurrealShort.count += 1
        
    def calculate_ordinal(cls, val: 'SurrealShort'):
        raise NotImplementedError
    
    def is_valid(self):
        raise NotImplementedError
    
    def __le__(self, other: 'SurrealShort'):
        return self == other or self < other
    
    def __add__(self, other):
        if isinstance(other, SurrealShort):
            left = self.left.intersection(other.left)
            right = self.right.intersection(other.right)
            return SurrealShort(left, right)
        raise TypeError("unsupported operand type(s) for +: 'SurrealNumber' and '{}'".format(type(other).__name__))
    
    def __mul__(self,value: 'SurrealShort'):
        raise NotImplementedError

    def __div__(self,value: 'SurrealShort'):
        raise NotImplementedError

    def __repr__(self):
        return 'SurrealNumber(left={}, right={})'.format(self.left, self.right)
    
    def __eq__(self, other):
        if isinstance(other, SurrealShort):
            return self.left == other.left and self.right == other.right
        return False
    
    def __lt__(self, other):
        if isinstance(other, SurrealShort):
            if self.left < other.left:
                return True
            elif self.left == other.left and self.right < other.right:
                return True
            else:
                return False
        raise TypeError("unorderable types: SurrealShort() < {}()".format(type(other).__name__))

    
        
        
        
