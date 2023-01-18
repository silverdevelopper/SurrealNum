from typing import List
import math
from Surreal_num_utils import *

class Surreal_Converter:
    @staticmethod
    def convert(val):
        if isinstance(val, int):
            return Surreal_Converter.convert_int(val)
        elif isinstance(val, float):
            return Surreal_Converter.convert_float(val)

    @staticmethod
    def convert_int(value: int):
        if value == 0:
            return Surreal_Finite.SurrealZero
        elif value == 1:
            return Surreal_Finite.SurrealOne
        elif value > 1:
            return SurrealShort(str(value), left=[Surreal_Converter.convert_int(value-1)], right=[])
        else:
            return SurrealShort(str(value),left=[],right=[Surreal_Converter.convert_int(value+1)])

    def convert_float(cls, value: float):
        return NotImplementedError


class Ordinal:
    def __init__(self, number: int = None):
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

    def __init__(self, name: str = None, left: list = [], right: list = []):
        #self.name = name if name else self.convert_to_rat
        self.name = name
        if (isinstance(left, list) and left != SurrealShort.ϕ) or isinstance(left, SurrealShort):
            self.left = left
        else:
            self.left: SurrealShort = SurrealShort.ϕ

        if (isinstance(right, list) and right != SurrealShort.ϕ) or isinstance(right, SurrealShort):
            self.right: SurrealShort = right  # list(set(right).sort())
        else:
            self.right: SurrealShort = SurrealShort.ϕ
        # self.is_valid()
        self.h = hash("{self.__repr()__}")
        SurrealShort.count += 1
       
    def convert_to_rat(self):
        res = 0
        if self==Surreal_Finite.SurrealZero:
            return 0
        elif self.right and self.left :
            self.right.sort()
            self.left.sort()
            res= math.sqrt(SurrealShort.convert_to_rat(self.right[0])*SurrealShort.convert_to_rat(self.left[-1]))
            +1/(2/(SurrealShort.convert_to_rat(self.right[0])-SurrealShort.convert_to_rat(self.left[-1])))
        elif not self.right:
            res= int(SurrealShort.convert_to_rat(self.left[0])+1)
        else:
            res= int(SurrealShort.convert_to_rat(-self.right[-1])+1)
        self.name = str(res)
        return res

    def calculate_ordinal(cls, val: 'SurrealShort'):
        raise NotImplementedError

    def is_valid(self):
        """
        if not isinstance(self.right,SurrealShort) or not isinstance(self.left,SurrealShort):
        """
        if self.left == [] or self.right == []:
            return True
        for a in self.left:
            for b in self.right:
                if not b <= a:
                    result = True
                else:
                    return False
        return result

    def __neg__(self):
        if self.left == [] and self.right == []:
            return self
        left = [-x for x in self.right]
        right = [-y for y in self.left]
        return SurrealShort(left=left, right=right)
        
    def __sub__ (self,value:'SurrealShort'):
        return self+-value
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
            result = y
        elif y == Surreal_Finite.SurrealZero:
            result = self
        elif isinstance(y, int):
            result = self + SurrealShort.convert_int(y)
        else:
            result = SurrealShort([y + a for a in x.left].extend(x + b for b in y.left), 
                                  [y + a for a in x.right].extend(x + b for b in y.right))
        return result

    def shorten(self):
        raise NotImplementedError

    def __mul__(self, value: 'SurrealShort'):
        if self and value:
        #return SurrealShort((self.left*value+self*value.left+-self.left*value.left, self.right*value+self*value.right+self*value.right+-self.right*value.right), (self.left*value+self*value.right+-self.left*value.right, self.right*value+self*value.left+-self.right*value.left))
            return SurrealShort([a*value+self*c-a*c for a in self.left for c in value.left].extend([b*value+self*d+self*d-b*d for b in self.right for d in value.right]),[a*value+self*d-a*d for a in self.left for d in value.right].extend([b*value+self*c-b*c for b in self.right for c in value.left]))
        return Surreal_Finite.SurrealZero
    def __div__(self, value: 'SurrealShort'):
        raise NotImplementedError
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.name:
            return f'SN({self.name })'
        return 'SN({} | {})'.format(self.left, self.right)

    def __eq__(self, y):
        
        if self <= y and y <= self:
            return True
        return False

    def leq(self, X: 'SurrealShort', Y: 'SurrealShort'):
        if len(X.left) and self.leq(Y, X.left[-1], X):
            return False
        elif len(Y.right) and self.leq(Y.right[0], X):
            return False
        else:
            return True

    def __le__(self, y):
        if self.left and y.right:
            for a in self.left:
                for b in y.right:
                    if ( y <= a and b <= self):
                        return False

        elif self.left:
            for a in self.left:
                if  y <= a:
                    return False
        elif y.right:
            for b in y.right:
                if b <= self:
                    return False
        return True
    
        raise TypeError("unorderable types: SurrealShort() < {}()".format(type(y)._name_))
   
    def __lt__(self, y):
        """
        if self.left and y.right:
            for a in self.left:
                for b in y.right:
                    if ( y < a and b < self):
                        return False

        elif self.left:
            for a in self.left:
                if  y < a:
                    return False
        elif y.right:
            for b in y.right:
                if b < self:
                    return False
        return True
        """
        if self !=y:
            return self<=y
        return False
   
    def __gt__(self,y):
        return not(self <= y)
    
    def __ge__(self,y):
        return not(self < y)

class Zero(SurrealShort):
    def __init__(self):
        self.left = []
        self.right = []

class Surreal_Finite:
    ϕ = []
    SurrealZero = SurrealShort("0", ϕ, ϕ)
    SurrealOne = SurrealShort("1", [SurrealZero], ϕ)
    SurrealMinusOne = SurrealShort("-1", ϕ, [SurrealZero])
    SurrealTwo = SurrealShort("2", [SurrealOne], ϕ)
    SurrealThree = SurrealShort("3", [SurrealTwo], ϕ)
    SurrealMinusTwo = SurrealShort("-2", ϕ, [SurrealMinusOne])
    SurrealMinusThree = SurrealShort("-3", ϕ, [SurrealMinusTwo])
    SurrealOneHalf=SurrealShort("1/2",[SurrealZero],[SurrealOne])
    SurrealMinusOneHalf=SurrealShort("1/2",[SurrealMinusOne],[SurrealZero])
    Üsreel=SurrealShort("666",[SurrealOne],[SurrealZero])
    MinÜsreel=SurrealShort("999",[SurrealZero],[SurrealMinusOne])
      
class Generator:
    days= {
        0 : [Surreal_Finite.SurrealZero]
    }
    edges = []
    @staticmethod
    def generate_day(day: int = 1):
        if day in Generator.days:
            return Generator.days
        
        for d in range(0,day,1):
            nodes = []
            Generator.days[d+1] = []
            for i,s in enumerate(Generator.days[d]): # iterate days in list
                l = SurrealShort(left=[s ],right = [ ])
                r = SurrealShort(left=[],right = [s ])
                
                
                if l.is_valid():
                    nodes.append((str(Surreal_Finite.SurrealZero),str(l) ) )
                    l.convert_to_rat()
                    Generator.days[d+1].append(l)
                    
                if r.is_valid():
                    nodes.append((str(Surreal_Finite.SurrealZero),str(r) ) )
                    r.convert_to_rat()
                    Generator.days[d+1].append(r)
                    
                suureals_until_the_day = []
                for dd in range(d+1):
                    suureals_until_the_day += Generator.days[dd]
                    
                for j,p in enumerate(suureals_until_the_day ):
                    if j != i:
                        x = SurrealShort(left= [p] ,right = [s] )
                        if x.is_valid():
                            #x.convert_to_rat()
                            nodes.append((str(p),str(s)))
                            Generator.days[d+1].append(x)
                            
                        x = SurrealShort(left= [s],right = [p] )
                        if x.is_valid():
                            #x.convert_to_rat()
                            nodes.append((str(s),str(p)))
                            Generator.days[d+1].append(x)
        Generator.edges = nodes
        return Generator.days
    
    @staticmethod
    def plot_generator():
        plot_graph(Generator.edges)
        
    def gen_day(day:int = 0):
        if day == 0:
            return Generator.days
        