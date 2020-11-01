#PF-Prac-1
def add_string(str1):
    #start writing your code here
    if len(str1)<3:
        return str1
    elif str1.endswith('ing')==True:
        str1+='ly'
    elif str1.endswith('ing')!=True:
        str1+='ing'
    return str1

str1="com"
print(add_string(str1))
