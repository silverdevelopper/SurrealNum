from typing import List
import math

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
            return S_F.SurrealZero
        elif value == 1:
            return S_F.SurrealOne
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
            self.value = S_F.SurrealZero

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
        #x=k/2n  (with k odd and n>0), just let xL=(k−1)/2n and xR=(k+1)/2n
    def convert_to_rat(self):
        if self==S_F.SurrealZero:
            return 0
        elif self.right and self.left :
            self.right.sort()
            self.left.sort()
            k=SurrealShort.convert_to_rat(self.right[0])*SurrealShort.convert_to_rat(self.left[-1])
            v=SurrealShort.convert_to_rat(self.right[0])-SurrealShort.convert_to_rat(self.left[-1])
            if v !=0:
                if k >= 0:
                    return abs(math.sqrt(k)+1/(2/v)) if self>S_F.SurrealZero else -abs(math.sqrt(k)+1/(2/v))
                else:
                    return abs(math.sqrt(-k)+1/(2/v)) if self >S_F.SurrealZero else -abs(math.sqrt(-k)+1/(2/v))
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
        self.left = [-x for x in self.right]
        self.right = [-x for x in self.left]
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
        if self == S_F.SurrealZero:
            result = y
        elif y == S_F.SurrealZero:
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
        if self == S_F.SurrealOne:
            return value 
        elif value == S_F.SurrealOne:
            return self
        elif self == S_F.SurrealMinusOne:
            return -value
        elif value == S_F.SurrealMinusOne:
            return self
        elif value == S_F.SurrealZero or self == S_F.SurrealZero:
            return S_F.SurrealZero
        else:
        #return SurrealShort((self.left*value+self*value.left+-self.left*value.left, self.right*value+self*value.right+self*value.right+-self.right*value.right), (self.left*value+self*value.right+-self.left*value.right, self.right*value+self*value.left+-self.right*value.left))
            return SurrealShort([a*value+self*c-a*c for a in self.left for c in value.left].extend([b*value+self*d+self*d-b*d for b in self.right for d in value.right]),[a*value+self*d-a*d for a in self.left for d in value.right].extend([b*value+self*c-b*c for b in self.right for c in value.left]))
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
class S_F:
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
        0 : [S_F.SurrealZero]
    }
    üsr_days={
        0 : [S_F.SurrealZero]
    }
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
                
                Generator.days[d+1].append(l)

                Generator.days[d+1].append(r)
                    
                suureals_until_the_day = []
                for dd in range(d+1):
                    suureals_until_the_day += Generator.days[dd]
                    
                for j,p in enumerate(suureals_until_the_day ):
                    if j != i:
                        x = SurrealShort(left= [p] ,right = [s] )
                        if x.is_valid():
                            Generator.days[d+1].append(x)
                            
                        x = SurrealShort(left= [s],right = [p] )
                        if x.is_valid():
                            Generator.days[d+1].append(x)
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
                 
    def gen_day(day:int = 0):
        if day == 0:
            return Generator.days
        

print( Surreal_Converter.convert(-2) <= S_F.SurrealMinusTwo )
print( Surreal_Converter.convert(-1) ==  S_F.SurrealMinusOne )
# print( S_F.SurrealMinusOne  ==  S_F.SurrealTwo )
# print( Surreal_Converter.convert(1) <= S_F.SurrealTwo )
# print( Surreal_Converter.convert(1) >= S_F.SurrealTwo )
# print( SurrealShort() <= S_F.SurrealZero )

# x = Surreal_Converter.convert(-2)
# y = S_F.SurrealMinusTwo 
# print(x.left,x.right)
# print(y.left,y.right)
print(SurrealShort("1", [S_F.SurrealTwo], [S_F.SurrealMinusOne]).is_valid())
#print(Generator.generate_day(4))
print( Surreal_Converter.convert(1).convert_to_rat())
print( S_F.SurrealTwo.convert_to_rat())  
print( S_F.SurrealMinusOneHalf.convert_to_rat(), S_F.SurrealMinusOne.convert_to_rat())
print( S_F.SurrealOneHalf.convert_to_rat())
print( S_F.Üsreel.is_valid())
print( S_F.Üsreel + S_F.MinÜsreel)
#print(S_F.SurrealTwo*S_F.SurrealOne)
print(Generator.üsr_day())
#print(S_F.SurrealMinusOne*S_F.SurrealOne)--yardım