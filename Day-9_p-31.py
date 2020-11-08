#PF-Prac-31
def sum_of_elements(num_list,number):
    index=0
    result_sum=0
    while index!=len(num_list):
        if num_list[index]==number and num_list[index+1]!=number:
            index+=2
        elif num_list[index]==number and num_list[index+1]==number:
            index+=1
        else:
            print(num_list[index])
            result_sum+=num_list[index]
            index+=1
    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))
