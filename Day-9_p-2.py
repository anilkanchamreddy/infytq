#PF-Prac-2
def bracket_pattern(input_str):
    #Remove pass and write your code here
    status=False
    if len(input_str)%2==0:
        if input_str.startswith('(')==True and input_str.endswith(')')==True:
            status = True
    return status

    
input_str="(())"
print(bracket_pattern(input_str))
