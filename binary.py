

def binarysearch(a,lower,higher,x):
	if higher>=lower:
		mid=(lower+higher)//2
		if a[mid]==x:
			return a[mid]
		elif a[mid]>x:
			return binarysearch(a,lower,mid-1,x)
		else:
			return binarysearch(a,mid+1,higher,x)
	else:
		return -1
a=[10,20,30,40,50,60]
x=int(input("enter the elment to search:"))
result=binarysearch(a,0,len(a)-1,x)
if result!=-1:
	print("element is present")
else:
	print("elment is not present")
