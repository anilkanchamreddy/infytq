#PF-Prac-27
def check_for_ten(num1,num2):
    #start writing your code here
    input_list=[num1,num2]
    return 10 in input_list or sum(input_list)==10
        
    
print(check_for_ten(10,9))
