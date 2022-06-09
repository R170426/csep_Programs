def compound_interest(p,r,n):
	for i in range(1,n+1):
			p=p*(1+r/100)
	return p
	
	def compound_interest(p,r,n):
		if(r==0):
			return p
	
	
p=int(input("enter the principle amount:"))
r=float(input("enter the interest:"))
n=int(input("enter the years:"))

amount=compound_interest(p,r,n)
ci=amount-p
print(ci)
