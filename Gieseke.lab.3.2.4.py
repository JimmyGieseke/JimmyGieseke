def DNAflipmirror(DNA):   #define flipped (same as 2.1)
    lsDNA = []
    for i in DNA:
        if i == 'A':
            lsDNA.append('T')
        if i == 'G':
            lsDNA.append('C')
        if i == 'C':
            lsDNA.append('G')
        if i == 'T':
            lsDNA.append('A')
    A = ''.join(lsDNA)
    return A
def DNAmirror(DNA):    #define mirror (same as 2.2)
    A = DNA[::-1]
    return A



validDNA = 'AGCT'


DNA = input(str('what is the first DNA sequence?')).upper()
DNA2 = input(str('what is the second DNA sequence?')).upper()

if all(i in validDNA for i in DNA) == True :      #test for validity
    print('DNA 1 valid')
    A = 1      #set A as 1 if valid
else:
    A = 0      
    print('DNA 2 invalid')

if all(i in validDNA for i in DNA2) == True :
    print('DNA 1 valid')
    A2 = 1     #set A as 1 if valid
else:
    A2 = 0
    print('DNA 2 invalid')

if A == 1 and A2 == 1:    #if both DNA 1 and DNA 2 is valid do the following, else do nothing
    if DNAmirror(DNA) == DNA2 or DNA == DNAmirror(DNA2) or DNAflipmirror(DNA) == DNA2 or DNA == DNAflipmirror(DNA2):
        print('part of same DNA sequence')  #if any of the combonations are equil they are part of the same sequence
  
    else:    #otherise they are the not part of the same
        print('DNA not part of the same string')
    
