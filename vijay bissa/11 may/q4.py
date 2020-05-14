A=int(input("Enter the size of Grid:- "))
if A<0:
    print(1)
else:
    arr=[0 for i in range(A+2)]
    arr[0]=arr[1]=1
    for i in range(2,A+1):
        for j in range(i+1):
            arr[i]=(arr[i]+arr[j]*arr[i-j-1])%(10**9+7)
    print(arr[A-1])