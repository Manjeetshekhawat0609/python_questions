# '''f = 1
# for n in range(20):
#     print(n, "! =", f)
#     n = n + 1
#     f = f * n '''

# # another method 

# '''f = 1
# n = 0
# for n in range(20):
#     print(n, "! =", f)
#     n = n + 1
#     f = f * n'''


f = 1
n = 1
while f < 1000000000:
    print(n, "! =",  f)
    n = n +1
    f = f * n
    