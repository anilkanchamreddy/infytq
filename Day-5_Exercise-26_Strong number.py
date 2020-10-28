#PF-Exer-26

def factorial(number):
    #remove pass and write your logic to find and return the factorial of given number
    product=1
    if number!=0:
        for count in range(1,(number+1)):
            product=product*count
    return product
    


def find_strong_numbers(num_list):
    #remove pass and write your logic to find and return the list of strong numbers from the given list
    num_t=0
    res_list=[]
    for num in num_list:
        temp_num=0
        temp_sum=0
        num_t=num
        while num_t!=0:
            temp_num=num_t%10
            temp_sum+=factorial(temp_num)
            num_t=num_t-temp_num
            num_t=int(num_t/10)
        if temp_sum == num and num!=0:
            res_list.append(num)
    return res_list


num_list=[145, 375, 100, 2, 10, 40585, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
