#PF-Prac-23
def divisible_by_sum(number):
    #start writing your code here
    status=False
    num_list=[int(x) for x in str(number)]
    if number%sum(num_list)==0:
        status=True
    return status

    
number=42
print(divisible_by_sum(number))
