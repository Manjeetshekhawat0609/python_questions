a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))

greatest = a
if b > greatest:
    greatest = b

if c > greatest:
    greatest = c

if d > greatest:
    greatest = d

print("Greatest number is: ", greatest) 