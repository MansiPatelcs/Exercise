# approach 1  slicing

l=[4,8,3,2,10,12,23]
# l_copy=l[:]
# print(l_copy)

# approach 2 extend

# l_copy=[]
# l_copy.extend(l)
# print(l_copy)

# approach 3 list()

# l_copy=list(l)
# print(l_copy)

# approach 4 copy

# l_copy=l.copy()
# print(l_copy)

# approach 5 list comprehension

l_copy=[i for i in l]
print(l_copy)
