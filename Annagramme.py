#Exercice 11
#1
M = [mot[:-1] for mot in open(r'C:\Users\emily\OneDrive\Documents\Obsidian Vault\Multimédia\Pdf\mots.txt')]
print(len(M))
#2
s='amere'
signature=tuple(sorted(s))
print(signature)
#3
D=dict()
for mot in M:
    signature=tuple(sorted(mot))
    if signature not in D:
        D[signature]=1
    else:
        D[signature]+=1
print(D[tuple(sorted('abandonner'))])
#D = dict () for k in L : D [ k ] = D . get (k ,0) + 1
#4
max=1
for c in D:
    if D[c] > max:
        max = D[c]
print(max)
#5
l=[]
for c in D:
    if D[c]==max:
        l+=[c]
print(l)
for T in l:
    for mot in M:
        if T==tuple(sorted(mot)):
            print(mot)
