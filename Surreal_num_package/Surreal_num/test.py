from .Surrel_num import SurrealShort,Surreal_Finite
a=SurrealShort()
b=SurrealShort(a,)
c=SurrealShort(None,b)

d = SurrealShort({1,2,3},{2,3,4})
print(a)
print(b)
print(c)
print(d)
