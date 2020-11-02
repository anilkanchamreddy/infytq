#PF-Prac-4
def find_nine(nums):
    #Remove pass and write your code here
    status=False
    if len(nums)>=4:
        count=4
    else:
        count=len(nums)
    for i in range(0,count):
        if nums[i]==9:
            status=True
    return status
    

nums=[1,1]
print(find_nine(nums))
