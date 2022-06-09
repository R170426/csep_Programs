import aptitude as apt

list1=eval(input("enter a list:"))
print(apt.average_calculate(list1))

distance=int(input("Enter distance"))
time=int(input("enter time"))
print(apt.speed_calculate(distance,time))

list2=eval(input("enter a list:"))
print(apt.addition(list2))

p=int(input("Enter principal amount:"))
t=int(input("Enter the time"))
r=int(input("Enter rate of interest:"))
print(apt.simple_interest(p,t,r))
