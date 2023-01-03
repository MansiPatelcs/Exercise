# approach 1  using for loop

s='welcome'
# count=0
# for i in s:
#     count=count+1
# print(count)

# approach 2 using while loop and slicing

# i=1
# count=0
# while s[count:]:
#     count=count+1
# print(count)

# approach 3
# print(len(s))

# approach 4 using join and count

str='x'

print(str.join(s))
print(str.join(s).count(str)+1)
