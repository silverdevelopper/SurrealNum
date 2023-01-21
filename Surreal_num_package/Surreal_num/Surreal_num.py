from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)
from typing import List
import math
#from Surreal_num_utils import *
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
            return SurrealShort( left=[Surreal_Converter.convert_int(value-1)], right=[], name=str(value))
        else:
            return SurrealShort(left=[],right=[Surreal_Converter.convert_int(value+1)], name=str(value))

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
    count = 0
    ϕ = []

    def __init__(self, left: list = [], right: list = [],name: str = None):
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
        #x=k/2n  (with k odd and n>0), just let xL=(k−1)/2n and xR=(k+1)/2n
    def convert_to_rat(self):
        if self==Surreal_Finite.SurrealZero:
            return 0
        elif self.right and self.left :
            self.right.sort()
            self.left.sort()
            k=SurrealShort.convert_to_rat(self.right[0])*SurrealShort.convert_to_rat(self.left[-1])
            v=SurrealShort.convert_to_rat(self.right[0])-SurrealShort.convert_to_rat(self.left[-1])
            if v !=0:
                if k >= 0:
                    return abs(math.sqrt(k)+1/(2/v)) if self>Surreal_Finite.SurrealZero else -abs(math.sqrt(k)+1/(2/v))
                else:
                    return abs(math.sqrt(-k)+1/(2/v)) if self >Surreal_Finite.SurrealZero else -abs(math.sqrt(-k)+1/(2/v))
            else:
                return 0
        elif not self.right:
            return int(SurrealShort.convert_to_rat(self.left[0])+1)
        elif not self.left:
            return -int(SurrealShort.convert_to_rat(self.right[-1])+1)
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
        if x == Surreal_Finite.SurrealZero:
            result = y
        elif isinstance(y, int):
            result = x + Surreal_Converter.convert_int(y)
        elif y == Surreal_Finite.SurrealZero:
            result = x
        else:
            p=[x + b for b in y.left]
            c=[x + b for b in y.right]
            s=[y + a for a in x.left]
            ş=[y + a for a in x.right]
            #s.extend(p)
            #ş.extend(c)
            result = SurrealShort(s+p, 
                                  ş+c)
        return result
    def shorten(self):
        for y in self.left:
            for x in self.left:
                if y.shorten()==x.shorten():
                    self.left.remove(y)
        for y in self.right:
            for x in self.right:
                if y.shorten()==x.shorten():
                    self.right.remove(y)
        return self
            
    def __mul__(self, value: 'SurrealShort'):
        if self == Surreal_Finite.SurrealOne:
            return value 
        elif value == Surreal_Finite.SurrealOne:
            return self
        elif self == Surreal_Finite.SurrealMinusOne:
            return -value
        elif value == Surreal_Finite.SurrealMinusOne:
            return -self
        elif value == Surreal_Finite.SurrealZero or self == Surreal_Finite.SurrealZero:
            return Surreal_Finite.SurrealZero
        else:
        #return SurrealShort((self.left*value+self*value.left+-self.left*value.left, self.right*value+self*value.right+self*value.right+-self.right*value.right), (self.left*value+self*value.right+-self.left*value.right, self.right*value+self*value.left+-self.right*value.left))
            return SurrealShort([a*value+self*c-a*c for a in self.left for c in value.left]+[b*value+self*d+self*d-b*d for b in self.right for d in value.right],[a*value+self*d-a*d for a in self.left for d in value.right]+[b*value+self*c-b*c for b in self.right for c in value.left])
    def __div__(self, value: 'SurrealShort'):
        raise NotImplementedError

    def __repr__(self):
        #if self.name:
        #    return f'({self.name })'
        return '({} | {})'.format(self.left, self.right)

    def __eq__(self, y):
        
        '''if len(self.left) != len(y.left) or len(self.right) != len(y.right):
            return False
        for i,_ in enumerate(self.right):
            if self.right[i] != y.right[i]:
                return False
        for i,_ in enumerate(self.left):
            if self.left[i] != y.left[i]:
                return False
        return True'''
       
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
    
        #raise TypeError("unorderable types: SurrealShort() < {}()".format(type(y)._name_))
   
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
class Surreal_Finite:
    ϕ = []
    SurrealZero = SurrealShort( ϕ, ϕ,"0")
    SurrealOne = SurrealShort( [SurrealZero], ϕ, "0")
    SurrealMinusOne = SurrealShort( ϕ, [SurrealZero],"-1")
    SurrealTwo = SurrealShort( [SurrealOne], ϕ,"2")
    SurrealThree = SurrealShort( [SurrealTwo], ϕ,"3")
    SurrealMinusTwo = SurrealShort( ϕ, [SurrealMinusOne],"-2")
    SurrealMinusThree = SurrealShort( ϕ, [SurrealMinusTwo],"-3")
    SurrealOneHalf=SurrealShort([SurrealZero],[SurrealOne],"1/2")
    SurrealMinusOneHalf=SurrealShort([SurrealMinusOne],[SurrealZero],"-1/2")
    Üsreel=SurrealShort([SurrealOne],[SurrealZero],"666")
    MinÜsreel=SurrealShort([SurrealZero],[SurrealMinusOne],"999")
      
class Generator:
    days= {
        0 : [Surreal_Finite.SurrealZero]
    }
    üsr_days={
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
                
                
        
                nodes.append((str(Surreal_Finite.SurrealZero),str(l) ) )
                l.convert_to_rat()
                Generator.days[d+1].append(l)
                    

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
                            x.convert_to_rat()
                            nodes.append((str(p),str(s)))
                            Generator.days[d+1].append(x)
                            
                        x = SurrealShort(left= [s],right = [p] )
                        if x.is_valid():
                            x.convert_to_rat()
                            nodes.append((str(s),str(p)))
                            Generator.days[d+1].append(x)
        Generator.edges = nodes
        return Generator.days
    
    def üsr_day(day: int = 1):
        if day in Generator.üsr_days:
            return Generator.üsr_days
        
        for d in range(0,day,1):
            Generator.üsr_days[-d-1]=[]
            Generator.üsr_days[d+1] = []
            for i,s in enumerate(Generator.üsr_days[d]): # iterate üsr_days in list
                l = SurrealShort(left=[s ],right = [ ])
                r = SurrealShort(left=[],right = [s ])
                Generator.üsr_days[d+1].append(l)
                Generator.üsr_days[d+1].append(r)
                    
                suureals_until_the_day = []
                for dd in range(d+1):
                    suureals_until_the_day += Generator.üsr_days[dd]
                    
                for j,p in enumerate(suureals_until_the_day):
                    if j != i:
                        if p == -s or p==s:
                            pass
                        x = SurrealShort(left= [p] ,right = [s] )
                        if x.is_valid():
                            Generator.üsr_days[d+1].append(x)
                        else:
                            Generator.üsr_days[-d-1].append(x)
                            
                        x = SurrealShort(left= [s],right = [p] )
                        if x.is_valid():
                            Generator.üsr_days[d+1].append(x)
                        else :
                            Generator.üsr_days[-d-1].append(x)
        return Generator.üsr_days
    #def plot_generator():
    #    plot_graph(Generator.edges)
        
    def gen_day(day:int = 0):
        if day == 0:
            return Generator.days
        
    def gen_day(day:int = 0):
        if day == 0:
            return Generator.days
        

#print( Surreal_Converter.convert(-2) <= Surreal_Finite.SurrealMinusTwo )
#print( Surreal_Converter.convert(-1) ==  Surreal_Finite.SurrealMinusOne )
#print( Surreal_Finite.SurrealMinusOne  ==  Surreal_Finite.SurrealTwo )
#print( Surreal_Converter.convert(1) <= Surreal_Finite.SurrealTwo )
#print( Surreal_Converter.convert(1) >= Surreal_Finite.SurrealTwo )
#print( SurrealShort() <= Surreal_Finite.SurrealZero )
#x = Surreal_Converter.convert(-2)
#y = Surreal_Finite.SurrealMinusTwo 
#print(x.left,x.right)
#print(y.left,y.right)
#print(SurrealShort("1", [Surreal_Finite.SurrealTwo], [Surreal_Finite.SurrealMinusOne]).is_valid())
#print(Generator.generate_day(4))
#print( Surreal_Converter.convert(1).convert_to_rat())
#print( Surreal_Finite.SurrealTwo.convert_to_rat())  
#print( Surreal_Finite.SurrealMinusOneHalf.convert_to_rat(), Surreal_Finite.SurrealMinusOne.convert_to_rat())
#print( Surreal_Finite.SurrealOneHalf.convert_to_rat())
#print( Surreal_Finite.Üsreel.is_valid())
#print( Surreal_Finite.Üsreel + Surreal_Finite.MinÜsreel)
#print(Surreal_Finite.SurrealTwo*Surreal_Finite.SurrealOne)
#print(Generator.üsr_day())
#print(Generator.generate_day(3))
#print(Surreal_Finite.Üsreel*Surreal_Finite.MinÜsreel)
#print(Surreal_Finite.SurrealOne*Surreal_Finite.SurrealTwo)
#print(Surreal_Finite.Üsreel+Surreal_Finite.MinÜsreel)
#print(Surreal_Finite.SurrealMinusOne*Surreal_Finite.SurrealOne)
x = Surreal_Converter.convert(1)
y = Surreal_Finite.SurrealThree
x+=5
print(x)
x.shorten()
print(x)
print(x.convert_to_rat())
b=Surreal_Finite.SurrealMinusOneHalf+Surreal_Finite.SurrealMinusOne
b.left
print(b.left[0])


