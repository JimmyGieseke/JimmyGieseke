DNA = input(str('what is the first DNA sequence?')).upper()
DNA2 = input(str('what is the second DNA sequence?')).upper()
#define DNA 1 and DNA 2
A = sum(a==b for a, b in zip(DNA, DNA2))
#sum of the times a is b in iterations a and b of DNA and DNA2 at the same time

print(A)  #print A
