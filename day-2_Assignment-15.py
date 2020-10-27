#PF-Assgn-15

def find_product(num1,num2,num3):
    product=1
    #write your logic here
    num_list=[num1,num2,num3]
    if 7 in num_list:
        index=num_list.index(7)
        new_num_list=num_list[index+1:]
    else:
        new_num_list=num_list
    if len(new_num_list)==0:
        product=-1
    else:
        for num in new_num_list:
            product=product*num
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(4,3,2)
print(product)
