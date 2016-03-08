validDNA = 'AGCT'  #set valid DNA

DNA = input(str('what is the DNA sequence?')).upper()  #input DNA in uppercase


if all(i in validDNA for i in DNA) == True :   #if all iterations of validDNA in DNA  are true do the rest
    print('valid')  #print valid
else:           #otherwise print invalid
    print('invalid')

