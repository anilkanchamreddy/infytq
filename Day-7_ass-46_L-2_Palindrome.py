#PF-Assgn-46

def nearest_palindrome(num):
    #start writitng your code here
    num_ber=str(num)
    if num_ber!=num_ber[::-1]:
        if len(num_ber)%2!=0:
            index=int((len(num_ber)-1)/2)
            new_num=num_ber[:index]
            result=new_num+num_ber[index:-index]+new_num[::-1]
            return result
        else:
            index=int(len(num_ber)/2)
            new_num=num_ber[:index]
            result=new_num+new_num[::-1]
            return result

number=1230
print(nearest_palindrome(number))
