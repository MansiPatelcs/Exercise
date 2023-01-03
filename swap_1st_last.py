#approch 1  # temparory variable

mylist=[12,35,56,24,9]
# size=len(mylist)
# print(size)
#
# a=mylist[0]
# mylist[0]=mylist[size-1]
# mylist[size-1]=a
#
# print(mylist)

# approach 2

# mylist[0],mylist[-1]=mylist[-1],mylist[0]
# print(mylist)

#approch 3 # using tuple

# get=(mylist[-1],mylist[0]) # packing
#
# mylist[0],mylist[-1]=get
# print(mylist)

# approach 4   # * operand

# start,*mid,end=mylist
#
# mylist=[end,*mid,start]
# print(mylist)

# approach 5 using pop()

first=mylist.pop(0)
last=mylist.pop(-1)

mylist.insert(0,last)
mylist.append(first)

print(mylist)

