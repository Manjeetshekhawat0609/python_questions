thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print (x)

# union 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# method 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"john", "elena"}
set4 = {"apple", "banana", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)