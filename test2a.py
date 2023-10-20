a= int(input("Enter side length a:"))
b= int(input("Enter side length b:"))
C= int(input("Enter side length c:"))
if a<b+C and b<a+C and C<a+b:
    print("You Can make triangle")
else:
    print("You cant make triangle!")
