#Exercice 31
from itertools import permutations
for s ,i ,x ,t ,r , o in permutations ( ' 0123456789 ' ,6):
    if int ( s + i + x )**2 == int ( t + r + o + i + s ):
        print(' trois = '+ t + r + o + i + s + ' six = '+ s + i + x )

for u , n , d , e , x in permutations (  '0123456789 ' , 5): 
    if int ( u + n )**2 + int(u+n) == int(d+e+u+x): 
        print ( ' un = '+ u+n +  'deux = '  + d+e+u+x )
