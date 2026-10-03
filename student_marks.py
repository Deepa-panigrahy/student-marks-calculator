name=input("enter your name:")
mark1=int(input("enter marks in physics:"))
mark2=int(input("enter marks in chemistry:"))
mark3=int(input("enter marks in math:"))
total=mark1+mark2+mark3
percentage=total/3
print(name)
print(total)
print(percentage,"%")
if percentage>=40:
    print("pass")
else:
    print("fail")