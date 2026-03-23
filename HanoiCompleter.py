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
#4
def solve (n ,A ,B , C ): 
  """ 
  int x int x int x int -> list ( of couples of int ) renvoie la suite des mouvements à effectuer pour déplacer les n disques supérieurs de la tige A vers la tige B ( C est la tige restante ) 
  """ 
  if n ==1: 
    return [( A , B )] 
  return solve (n -1 ,A ,C , B )+[( A , B )]+ solve (n -1 ,C ,B , A )
#5
def solve2 (H , N ): 
  """ 
  Hanoi object x int -> résout le problème des tours de Hanoï ( pour H ) avec N disques 
  """ 
  petit = 0 
  if N %2==0: 
    sens = 1
  else : 
    sens = 2  
  H . move ( petit , petit + sens ) 
  petit = petit + sens 
  for n in range ((2** N -2)//2):
    try : 
      H . move (( petit +1)%3 ,( petit +2)%3) 
    except : 
      H . move (( petit +2)%3 ,( petit +1)%3) 
    H . move ( petit ,( petit + sens )%3) 
    petit = ( petit + sens )%3
    
H = Hanoi (5 ,0.5) 
solve2 (H ,5) 
H = Hanoi (10 ,0.01) 
solve2 (H ,10)
