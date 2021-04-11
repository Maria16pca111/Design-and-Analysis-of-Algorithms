# find the square root of a given no
# using the Iterative Method
import math
def iseven(m):
    flag = False
    if(m % 2 == 0):
        flag = True
    return flag;
def betterguess(m,a):
    betterguessarr = []
    differencearr = []
    flag = False
    for i in a:
        difference = m - round (i * i)
        if not(difference < 0):
            betterguessarr.append(i)
            differencearr.append(difference)
            differencearr.sort()
            betterguessarr.sort()
    if len(betterguessarr) > 0:   
        flag = True 
        result1 = betterguessarr[len(betterguessarr)-1] 
    if len(differencearr) > 0: 
        flag = True
        result = differencearr[len(differencearr)-1]
    split = "&"
    if flag == True:
        return result1,split,result
    else:
        return 0

def Squareroot(m):
    #initial guess.
    flag = True
    a=[]
    result=[]
    print("Given no is ",m)
    flag = iseven(m)
    if(flag == False):
        start = 3
        Jump = 2
    else:
        start = 2
        Jump = 2
    for j in range(start,m,Jump):
        n = m % j      
        if(n == 0):
            a.append(j)  
        else:
            continue 
    if not (len(a) == 1):  
        guess = betterguess(m,a)    
        if not (guess == 0):
            m = guess[0]
            m1 = guess[2]    
    for i in a:
        #a_float = n
        #formatted_float = "{:.2f}".format(a_float)
        m = round(m,2)
        n = round(i * i,2)       
        while(n != m): 
            #n = "{:.2f}".format(n)  
            n = round(n,2)        
            if(n > m):
                n -=  1                
            elif (n < m):
                n += 0.1
            else:
                if(n == m):
                    print("SquareRoot by Using Iterative Method Result is",n) 
                else:
                    continue
    print("SquareRoot by Using Iterative Method Result is",n) 
    return "Success"
print (Squareroot(64))

def iseven(m):
    flag = False
    if(m % 2 == 0):
        flag = True
    return flag;
def betterguess(m,a):
    betterguessarr = []
    differencearr = []
    for i in a:
        difference = m - round (a * a)
        betterguessarr.append(i)
        differencearr.append(difference)
        differencearr.sort()
        betterguessarr.sort()
        result1 = betterguessarr[len(betterguessarr-1)] 
        result = differencearr[len(differencearr-1)]
    return result1,result


        
