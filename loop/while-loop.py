print("\n using while loop")
i = 0
while i < 5:
    if i == 3:
        break #exit the loop when i is 3
    print(i)
    i += 1

print("\n while")
i = 1
while i < 6:
    print(i)
    i +=  1

print("\n while continue")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("\n  while else")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is longer less than 6")