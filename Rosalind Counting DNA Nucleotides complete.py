DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
newdna = tuple(DNA)
A = []
C = []
G = []
T = []

for i in newdna:
    if ord(i) == 65:
        A.append('A')
    elif ord(i) == 67:
        C.append('C')
    elif ord(i) == 71:
        G.append('G')
    elif ord(i) == 84:
        T.append('T')
print(len(A) , len(C), len(G), len(T))