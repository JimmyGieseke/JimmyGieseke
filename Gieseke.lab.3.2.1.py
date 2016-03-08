DNA = input(str('what is the DNA sequence?'))   #input string

lsDNA = []   #start new list
for i in DNA:    #for all values DNA
    if i == 'A':          #if DNA is A the add T to the end of lsDNA
        lsDNA.append('T') 
    if i == 'G':         #if DNA is G the add C to the end of lsDNA
        lsDNA.append('C')
    if i == 'C':          #if DNA is C the add G to the end of lsDNA
        lsDNA.append('G')
    if i == 'T':            #if DNA is T the add A to the end of lsDNA
        lsDNA.append('A')
A = ''.join(lsDNA)         #arrnage the list
print(A)         #print list
