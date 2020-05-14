num=int(input("Enter the number to find Square Root:-"))
f=0
if(num==0 or num==1):
	print(num)
st=1
end=num
while(st<=end):
	mid=(st+end)//2
	if(mid**2==num):
		print(mid)
		f=1
	if(mid**2<num):
		st=mid+1
		ans = mid
	else:
		end=mid-1
if(f==0):
	print(ans)
