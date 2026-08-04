# num = int(input("enter a number: "))

# if num <= 1:
#     print(num, "is not a prime no.")
# else :
#     is_prime = True

#     for i in range (2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, "is a prime no.")
#     else:
#         print(num,"is not a prime no.")



# num = int(input("enter a number: "))

# if num <= 1:
#     print(num, "is not a prime no.")
# else :
#     is_prime = True

#     for i in range (2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, "is a prime no.")
#     else:
#         print(num,"is not a prime no.")               


n = int(input("Enter the value of N: "))

print("Prime numbers are:")

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ") 