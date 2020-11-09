#PF-Prac-37
def sum_of_list(num_list): 
    #Start writing your code here
    lst=num_list
    if len(lst)==0:
        return 0
    return lst[0] + sum_of_list(lst[1:])
	#Do not alter the below line

num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)
