#PF-Assgn-36
def create_largest_number(number_list):
    #remove pass and write your logic here
    number_list.sort()
    result=''
    for i in number_list[::-1]:
        result+=str(i)
    return result
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
