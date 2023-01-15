from typing import List

class Surreal_Converter:
    @staticmethod
    def convert(val):
        if isinstance(val,int):
            return Surreal_Converter.convert_int(val)
        elif isinstance(val,float):
            return Surreal_Converter.convert_float(val)
    
    @staticmethod
    def convert_int(value:int):
        if value == 0:
            return Surreal_Finite.SurrealZero
        elif value == 1:
            return Surreal_Finite.SurrealOne
        elif value > 1:
            return SurrealShort(str(value) ,left= [Surreal_Converter.convert_int(value-1) ],right=[])
        else:
            return SurrealShort(right=[Surreal_Converter.convert_int(value+1)],left=[])
    
    def convert_float(cls,value:float):
        return NotImplementedError

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
    
    def __init__(self,name:str = None, left: list = [], right: list = []):
        self.name = name
        if (isinstance(left,list) and left != SurrealShort.ϕ) or isinstance(left,SurrealShort):
            self.left = left
        else:
            self.left:SurrealShort = SurrealShort.ϕ
            
        if (isinstance(right,list) and right != SurrealShort.ϕ ) or isinstance(right,SurrealShort) :
            self.right:SurrealShort  = right # list(set(right).sort())
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
        if self == Surreal_Finite.SurrealZero:
            result =  y
        elif y == Surreal_Finite.SurrealZero:
            result = self
        elif isinstance(y,int):
            return [z+y for z in self]
        else:
            result = SurrealShort([[y + a for a in x.left] ,[x + b for b in y.left]],[[y + a for a in x.right], [x + b for b in y.right]] )        
        return result
    
    def __mul__(self,value: 'SurrealShort'):
        return SurrealShort((self.left*value+self*value.left+-self.left*value.left,self.right*value+self*value.right+self*value.right+-self.right*value.right),(self.left*value+self*value.right+-self.left*value.right,self.right*value+self*value.left+-self.right*value.left))
    
    def __div__(self,value: 'SurrealShort'):
        raise NotImplementedError

    def __repr__(self):
        if self.name:
            return f'SurrealNumber({self.name })'
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
        
    def leq(self,X:'SurrealShort',Y:'SurrealShort'):
        if len(X.left) and self.leq(Y,X.left[-1],X):
            return False
        elif len(Y.right) and self.leq(Y.right[0],X):
            return False
        else:
            return True
    
            
    def __le__(self, y):
        
        if len(self.left) == 0:
            return False
        
        if len(self.right) == 0:
            return False
        
        elif self.left and not y.right:
            if not y <= self.left:
                return True
            return False
        elif y.right and not self.left:
            if not y.right <= self:
                return True
            return 0
        else:
            return True
                
            raise TypeError("unorderable types: SurrealShort() < {}()".format(type(y)._name_))
    
class Zero(SurrealShort):
    def __init__(self):
        self.left = []
        self.right = []  
class Surreal_Finite:
    ϕ = []   
    SurrealZero = SurrealShort("0", ϕ, ϕ ) 
    SurrealOne  = SurrealShort("1", [ SurrealZero ], ϕ ) 
    SurrealMinusOne  = SurrealShort("-1", ϕ, [ SurrealZero ] ) 
    SurrealTwo  = SurrealShort("2", [SurrealOne], ϕ ) 
    SurrealThree  = SurrealShort("3", [SurrealTwo], ϕ )  
    SurrealMinusTwo  = SurrealShort("-2", ϕ, [SurrealOne] ) 