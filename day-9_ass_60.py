#PF-Assgn-60
def remove_duplicates(value):
    #start writing your code here
    new_value=''
    for i in value:
        if i not in new_value:
            new_value+=i
    return new_value

print(remove_duplicates("1122334455ababzzz@@@123#*#*"))
