hight = int(input("how high do you want the pyramid to be? "))  #ask for hight of pyrimid
char = input('what do you want to make the pyrimid out of? ')
for pyr in range(1, hight+1):         #while pyr is from one to hight+1 do the following
    print(char*pyr)               #print the string char the number of time pyr is equil to
