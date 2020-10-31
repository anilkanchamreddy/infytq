#PF-Assgn-59
def check_perfect_number(number):
    #start writing your code here
    divisor_list=[]
    for i in range(1,int(number/2)+1):
        if number%i==0:
            divisor_list.append(i)
    if number==0:
        return False
    else:
        return sum(divisor_list)==number


def check_perfectno_from_list(no_list):
    #start writing your code here
    new_num_list=list()
    for num in no_list:
        if check_perfect_number(num)==True:
            new_num_list.append(num)
    return new_num_list


perfectno_list=check_perfectno_from_list([87, 76, 567, 99, 0])
print(perfectno_list)
