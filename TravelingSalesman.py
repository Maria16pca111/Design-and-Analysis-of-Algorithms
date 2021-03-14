# find the TravelingSalesman Problem 
import random
def TravelingSalesman(arr1,arr2):
    flag=False 
    maxcost = 0   
    totalfare = 0
    for x in arr1:
        maxcost = maxcost + totalfare        
        for y in arr2:
            cost = random.randint(1,20)                      
            print ("Fare Expenses for",x, "Circle",y ," ",cost)
            totalfare = totalfare + cost             
        print("Visitited City",x)             
        print ("Visited City Total Expenses",totalfare)
    if (maxcost > totalfare):
        salary = min(maxcost,250)
        flag = True
    return salary, flag
arr1=["Trichy","Chennai","Koimbatore","Madurai","Trichy"]
arr2=[1,2,3,4,1]             
print(TravelingSalesman(arr1,arr2))       

