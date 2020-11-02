#PF-Prac-6
def list123(nums):
    #start writing your code here
    status=False
    for i in range(0,len(nums)-2):
        print('f')
        if nums[i]==1and(nums[i+1]==2 and nums[i+2]==3):#and (nums[i+1]==2 and nums[i+2]==3):
            print(i,'1')
            status=True
    return status

nums=[1,0,5,6,1]
print(list123(nums))
