hight = int(input('hight of pyrimid? '))   #inputs hight of pyrimid
char = input('input buliding block of pyrimid')
A = len(char)   #find how many charictars char is
for i in range(1,hight+1):              # for hight one to hight+1 do the following
# put in number of spaces equil to hight+1-i
#then add the charictar char the same number as hight (so that each line of the left side of the pyrimid ends at the same point for every i)
# then add more char for the second side of the pyrimid
   print (" "*(hight+1-i)*A+char*i+char*(i-1))
           #for every carictar 'char' is, add another space
