#Exercice 26
#1
from hanoi_tkinter import Hanoi 
H = Hanoi (3 ,1.5)
H . move (0 ,2) 
H . move (0 ,1) 
H . move (2 ,1) 
H . move (0 ,2) 
H . move (1 ,0) 
H . move (1 ,2) 
H . move (0 ,2)
#3
def solve (H ,n ,A ,B , C ): 
  """ 
  Hanoi object x int x int x int x int -> déplace les n disques supérieurs de la tige A vers la tige B ( C est la tige restante ) 
  """ 
  if n ==1: 
    H . move (A , B ) 
  else : 
    solve (H ,n -1 ,A ,C , B ) 
    H . move (A , B ) 
    solve (H ,n -1 ,C ,B , A ) 
H = Hanoi (5 ,0.5) 
solve (H ,5 ,0 ,2 ,1) 
H = Hanoi (10 ,0.01) 
    solve (H ,10 ,0 ,2 ,1)
