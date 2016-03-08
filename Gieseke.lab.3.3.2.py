DNA = input(str('what is the first DNA sequence?')).upper()
DNA2 = input(str('what is the second DNA sequence?')).upper()


if len(DNA)>len(DNA2):       #Loop through each possible start for a substring
    DNA, DNA2 = DNA2, DNA
substr = ""   
for start in range(len(DNA)):     #Loop through each possible ending for the current start
    for end in range(start,len(DNA)):
        sub = DNA[start:end+1]    #if it's in the other string, it's common
        if sub in DNA2:
    
            if len(sub)>len(substr):  #if it's longer than the current longest common substring found0
                substr = sub   #it's the new longest common substring
        
print (substr) #print
