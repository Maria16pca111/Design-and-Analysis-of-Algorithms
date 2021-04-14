import math
def SquareRoot1(m):
    flag = False
    CustomGuess = []
    count = 0
    # taking initial guess to find out the squareroot    
    if(m%2)==0:
        evenorodd = 2
    else:
        evenorodd = 3
    if(m == 0):
        print("Square root Values are known to be zero")
    elif(m == 1):
        print ("square root values are known to be one")
    else:
        n = round(m/2)
        for i in range(2,n,evenorodd):
            if(m % i) == 0:
                # append the data for taking the divisor 
                CustomGuess.append(i)
                count += 1
    for z in range(1,count):
        a = 0
        guess = CustomGuess[z]
        guessresult = float((guess + (m/guess))/2)
        a = guessresult
        a = a*a
        m = float(m)
        if(a == m):
            flag = True
            print("Square root is known to be",guessresult)
            break
        else:
           continue
    return flag
m = input("Enter your value to be find square root: ")
m = int(m)
print(SquareRoot1(m))




            

           



