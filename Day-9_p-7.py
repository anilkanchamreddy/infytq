#PF-Prac-7
def seed_no(number,ref_no):
    #start writing your code here
    status=False
    result=number
    digit_list=[int(x) for x in str(number)]
    for i in digit_list:
        result*=i
    if result==ref_no:
        status=True
    return status

number=123
ref_no=738
print(seed_no(number,ref_no))
