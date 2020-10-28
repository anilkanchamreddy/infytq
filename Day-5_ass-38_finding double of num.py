#PF-Assgn-38

def check_double(number):
    #Remove pass and write your logic here
    double_number=number*2
    number_string=sorted(str(number))
    double_number_string = sorted(str(double_number))
    return (number_string==double_number_string)

#Provide different values for number and test your program
print(check_double(125874))
