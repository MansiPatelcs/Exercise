l=[2,3,4,5]

# def greater(n):
#     for i in l:
#         if i>n:
#             return True
#         return False
#
# print(greater(1))
# print(greater(5))

print(all(i>1 for i in l))
print(all(i>4 for i in l))
