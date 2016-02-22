r = int(input('what is the radius? '))   #ask for input
#print(range(r+1,0,-1))

for cir_top in range(r,0,-2):                    #for the top of the circle use range r to 0 (skipping steps to make it look pretty)
    y1 = int((r**(2)-cir_top**(2))**(.5))    #solving for y = sqrt(r^2-x^2) where x is defined by the range
    print(" "*(r+1-y1)+'x'+" "*(2*y1)+'x')   #print the top half


for cir in range(0,r+1,2):      #for the bottom use range 0 to r
    y = int((r**(2)-cir**(2))**(.5))     # same thing as top half
    print(" "*(r+1-y)+'x'+" "*(2*y)+'x')   #print bottom half
    
