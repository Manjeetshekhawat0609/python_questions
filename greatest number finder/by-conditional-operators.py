a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))

greatest = a if (a >= b and a >= c and a >= d) else \
           b if (b >= c and b >= d) else \
           c if (c >= d) else d

print("Greatest number is: ", greatest)