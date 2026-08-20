myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

# duplicate not shown
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# true = 1; false = 0;
thisset = {"apple", "banana", "cherry", True , 1, 2}
print(thisset)

# remove bracket
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# check name
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# add name
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#update set
thisset = {"apple", "banana", "cherry"}
tropical = ("pineapple", "mango", "papaya")
thisset.update(tropical)
print(thisset)

# remove
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#empty set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print (x)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)