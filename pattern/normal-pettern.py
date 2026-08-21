print("\nnormal pattern")
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


print("\nright angle triangle pattern")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\nopposite")
n = 5
for i in range(n,0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\nnumber")
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("\nsame number")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()