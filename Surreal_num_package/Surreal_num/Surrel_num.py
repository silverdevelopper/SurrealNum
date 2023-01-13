from typing import List

class Ordinal:
    def __init__(self, number:int = None):
        if number:
            self.value = number
        else:
            self.value = Surreal_Finite.SurrealZero
            
    def __repr__(self) -> str:
        return str(self.value)


class SurrealShort:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """
    
    calculated_surreals = {}
    count = 10000
    ϕ = []
    
    def __init__(self,name:str = "", left:'SurrealShort' = None, right:'SurrealShort' = None):
        self.name = name
        if (isinstance(left,List) and left != SurrealShort.ϕ ) or isinstance(left,SurrealShort):
            self.left:SurrealShort = left
        else:
            self.left:SurrealShort = SurrealShort.ϕ 
            
        if (isinstance(right,List) and left != SurrealShort.ϕ ) or isinstance(right,SurrealShort) :
            self.right:SurrealShort  = right
        else:
            self.right:SurrealShort  = SurrealShort.ϕ 
        #self.is_valid()
        self.h = hash("{self.__repr()__}")
        SurrealShort.count += 1
        
    def calculate_ordinal(cls, val: 'SurrealShort'):
        raise NotImplementedError
    
    def is_valid(self):
        if not isinstance(self.right,SurrealShort) or not isinstance(self.left,SurrealShort):
            return True
        if not self.left <= self.right:
            return True
        return 0
    
    def __neg__(self):
        self.left=-self.left if self.left != set() else set()
        self.right=-self.right if self.right != set() else set()
    
    def __le__(self, y: 'SurrealShort'):
        if not isinstance(y,SurrealShort) or not isinstance(self,SurrealShort):
            return True
        return self == y or self < y

    ## TODO: Implement this method regarding surreal numbers addition. (Addition A surreal)
    """
    Let a and b is surreal numbers:
    a + b = ?
    (1,2 | 2,3) + (3,4,5 | 6,7,8):
    
        a.l + b = (1,2) + (3,4,5 | 6,7,8) = (b,4,5,6 | )
    
    """
    def __add__(self, y):
        x = self
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """
        result = None
        if isinstance(self,Zero):
            result =  y
        elif isinstance(y,Zero):
            result = self
        elif isinstance(y,int):
            return [z+y for z in self]
        else:
            result = SurrealShort([[y + a for a in x.left] ,[x + b for b in y.left]],[[y + a for a in x.right], [x + b for b in y.right]] )        
        #raise TypeError("unsupported operand type(s) for +: 'SurrealNumber' and '{}'".format(type(y)._name_))
        return result
    
    def __mul__(self,value: 'SurrealShort'):
        return SurrealShort((self.left*value+self*value.left+-self.left*value.left,self.right*value+self*value.right+self*value.right+-self.right*value.right),(self.left*value+self*value.right+-self.left*value.right,self.right*value+self*value.left+-self.right*value.left))
    
    def __div__(self,value: 'SurrealShort'):
        raise NotImplementedError

    def __repr__(self):
        return 'SurrealNumber(left={} | right={})'.format(self.left, self.right)
    
    def __eq__(self, y):
        if len(self.left) != len(y.left) or len(self.right) != len(y.right):
            return False
        for i,_ in enumerate(self.right):
            if self.right[i] != y.right[i]:
                return False
        for i,_ in enumerate(self.left):
            if self.left[i] != y.left[i]:
                return False
        return True
            
    
    def __lt__(self, y):
        if self.left and y.right:
            if not y <= self.left and not y.right <= self:
                return True
            return False
        elif self.left and not y.right:
            if not y <= self.left:
                return True
            return False
        elif y.right and not self.left:
            if y.right <= self:
                return True
            return 0
        else:
            return True
            
        raise TypeError("unorderable types: SurrealShort() < {}()".format(type(y)._name_))
    
    
class Surreal_Finite:
    ϕ = []   
    SurrealZero = SurrealShort("0", ϕ, ϕ ) 
    SurrealOne  = SurrealShort("1", [ SurrealZero ], ϕ ) 
    SurrealMinusOne  = SurrealShort("-1", ϕ, [ SurrealZero ] ) 
    SurrealTwo  = SurrealShort("2", [SurrealOne], ϕ ) 
    SurrealThree  = SurrealShort("3", [SurrealTwo], ϕ )  
    SurrealMinusTwo  = SurrealShort("-2", ϕ, [SurrealOne] ) 
    
a=SurrealShort(left=[Surreal_Finite.SurrealZero])
b=SurrealShort(left = a,right = None)
c=SurrealShort(left= None,right= b)

d = SurrealShort( left= [1,2,3],right= [2,3,4])
e = SurrealShort( left= [1,2,3],right= [2,3,4])
print(b)
print(c)
print( SurrealShort() == Surreal_Finite.SurrealOne)
print( SurrealShort() == Surreal_Finite.SurrealZero)
print(d == e)
