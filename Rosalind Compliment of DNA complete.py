DNA = 'AAAACCCGGT'
DNAlist = list(DNA)
listreversed = reversed(DNAlist)
answer = []
for i in listreversed:
    if ord(i) == 65:
        answer.append('T')
    elif ord(i) == 67:
       answer.append('G')
    elif ord(i) == 71:
        answer.append('C')
    elif ord(i) == 84:
       answer.append('A')
actual = ''.join(answer)
print(actual)
#test = ''.join(ans)
#print(test)