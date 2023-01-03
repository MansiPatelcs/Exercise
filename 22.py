list = [1,2,4,3,4,5,4]

print(list.count(4))

def list(nums):
    result=0
    for num in nums:
        if num==4:
            result=result+1
    return result
print(list([1,2,4,3,4,5,4]))
print(list([1,2,4,3,4,5,4,4,4,44,4]))
