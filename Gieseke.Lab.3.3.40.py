DNA = input(str('what is the first DNA sequence?')).upper()

Ref1 = 'GCTCAAGCCTAGCTACTAGCAGTT'      #set referance dnas
Ref2 = 'ACTCAAGCATAGCTCCATGCGTCCA'
Ref3 = 'AGCTAAGCTTAGCTCCATGCG'
lsDNAmatch = list()    #start new list
validDNA = 'AGCT'   #set valid dna values

def bestmatch(DNA, referance):
        if len(DNA)>len(referance):       #Loop through each possible start for a substring
            DNA, referance = referance, DNA
        substr = ""   
        for start in range(len(DNA)):     #Loop through each possible ending for the current start
            for end in range(start,len(DNA)):
                sub = DNA[start:end+1]    #if it's in the other string, it's common
                if sub in referance:
    
                    if len(sub)>len(substr):  #if it's longer than the current longest common substring found0
                        substr = sub   #it's the new longest common substring
        
        lsDNAmatch.append(substr) #Add to list

if all(i in validDNA for i in DNA) == True :
    A = 1   #if valid add set A as 1
else:
    print('DNA invalid')   


if A == 1:   #if dna is valid do the following

    bestmatch(DNA, Ref1)      #run function from DNA and each referance
    bestmatch(DNA, Ref2)
    bestmatch(DNA, Ref3)
    
    if max(lsDNAmatch) == lsDNAmatch[0]:   #if the longest match is in ref 1 print:
        print('best match ref 1') 
    elif max(lsDNAmatch) == lsDNAmatch[1]:  #if longest match is in ref2 print:
        print('best match ref 2')
    elif max(lsDNAmatch) == lsDNAmatch[2]:  #if longest match in in ref3 print:
        print('best match ref 3')
            
else:
    print('No DNA match')   #if there is no match print
