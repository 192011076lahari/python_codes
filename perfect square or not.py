n=float(input("enter a no:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum== n):
    print("it is a perfect number",n)
else:
    print("it is not a perfect number",n)
