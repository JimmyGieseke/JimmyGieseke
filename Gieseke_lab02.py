#Jimmy Gieske
expr = str('expression')      #define expr
Anslist = list()            #create new list to save answers
while expr != 'end':          #run until expr = end
    expr = str(input("(type end to stop) enter expression in form of number+number: ")) #user inputs expression
    end = len(expr)-1
    if expr.find('+') == 0 or expr.find('*') == 0 or expr.find('-') == 0 or expr.find('/') == 0:
        print('you done goofed')     #if there is a one of the things at the front then print

    elif expr.find('+') == end or expr.find('*') == end or expr.find('-') == end or expr.find('/') == end:
        print('you done goofed')
        
    elif expr[expr.find("+")] == '+':    #if there is a + do this stuff
        num1 = int(expr[:expr.find("+")])      #num1 is from the begining to the +
        num2 = int(expr[(expr.find("+")+1):])   #num2 is from the + (plus 1) to the ed
        ans = num1 + num2                      #addiion 
        print(expr,'=',ans)                    #print answer
        Q = str(ans)                         # set ans as a string
        A = str(expr + '=' + Q)             #set A as the expression anad answer in a single string
        Anslist.insert(0,A)                   #add A to this list
        
    elif expr[expr.find("*")] == '*':      #if there is a * do this stuff
        nums1 = int(expr[:expr.find("*")])
        num2 = int(expr[(expr.find("*")+1):])
        ans = num1 * num2
        print(expr,'=',ans)
        Q = str(ans)
        A = str(expr + '=' + Q)
        Anslist.insert(0,A)
        
    elif expr[expr.find("/")] == '/':      #if there is a / do this stuff
        num1 = int(expr[:expr.find("/")])
        num2 = int(expr[(expr.find("/")+1):])
        ans = num1 / num2
        print(expr,'=',ans)
        Q = str(ans)
        A = str(expr + '=' + Q)
        Anslist.insert(0,A)
        
    elif expr[expr.find("-")] == '-':      #if there is a - do this stuff
        num1 = int(expr[:expr.find("-")])
        num2 = int(expr[(expr.find("-")+1):])
        ans = num1 - num2
        print(expr,'=',ans)
        Q = str(ans)
        A = str(expr + '=' + Q)
        Anslist.insert(0,A)
        
    elif expr == 'end':     #if end is typed in, the program prints goodbye and ends
        print('goodbye')

    elif expr == 'last':            # if last is typed in, it prints the last 3 expression and answers
        print(Anslist[0:3])
        
    else :
        print('You did something wrong')       #if no sign print and run again
        
            
    
