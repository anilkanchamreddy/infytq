#PF-Prac-24
def find_gcd(num1,num2):
    #start writing your code here
    result=0
    if num1<num2:
        small=num1
    else:
        small=num2
    for i in range(1,small+1):
        if num1%i==0 and num2%i==0:
            result=i
    return result

num1=45
num2=9
print(find_gcd(num1,num2))
