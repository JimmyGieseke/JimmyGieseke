x1 = int(input('start of range '))  #ask for lower range
x2 = int(input('end of range '))   #ask for higher range
scale = int(input('scaling factor '))  #ask for scaling factor
for x in range(x1,x2+1):         #from range x1 to x2 do the following stuff
    y = int(((x)**(2))/scale)    #find all y values for the range of x
    #print(' ' * y + 'x'0
Q = range(y)         #find the start and end of y
W = max(Q)       #find the highest value of y
#print(W)
for prab in range(W,0,-1):                #from the highest value of y(W) to zero counting down to the followig
    dis = int((prab*scale)**(.5))    #find the x values for the y values
    print(" "*(W-dis)+'x'+" "*(2*dis)+'x')    # print the porabola
