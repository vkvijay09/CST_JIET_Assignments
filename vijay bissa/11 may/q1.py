def findSingle( ar, n): 
      
    res = ar[0] 
       
    for i in range(1,n): 
        res = res ^ ar[i] 
      
    return res 
  
 
print("Enter The Numbers:-  ")
ar= list(map(int,input().split()))
print ("Element occuring once is", findSingle(ar, len(ar))) 
