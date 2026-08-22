print("\n using for loop")
for i in range(5):
    if i == 3:
        break #exit the loop when i is 3
    print(i)


print("\n for continue")
for i in range(5):
    if i == 3:
        continue  # skip the rest  of the code for i = 3
    print(i)

print("\n for pass")
for i in range(5):
    if i == 3:
        pass  # placeholder for future code
    print(i)

print("\n for break")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print("\n for break")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
