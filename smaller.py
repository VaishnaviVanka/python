a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if a<b and a<c:
    print(a,"a is smaller")
elif b<a and b<c:
    print(b, " b is smaller")
elif c<a and c<b:
    print(c," c is smaller")
elif a==b==c:
    print(a ," a is smaller")
