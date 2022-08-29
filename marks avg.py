sub_1=int(input("enter marks:"))
sub_2=int(input("enter marks:"))
sub_3=int(input("enter marks:"))
avg=(sub_1+sub_2+sub_3)/3
if(avg>=90):
    print("grade:A")
elif(avg>=80):
     print("grade:B")
elif(avg>=70):
     print("grade:C")
    
elif(avg>=60):
     print("grade:D")
else:
     print("grade:F")
