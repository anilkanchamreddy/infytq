#PF-Assgn-58
def validate_credit_card_number(card_number):
    #start writing your code here
    str_card_no=str(card_number)
    card_list=[]
    card_double_list=[]
    card_list=[int(str_card_no[i]) for i in range(0,len(str_card_no),2)]
    card_double_list=[x*2 for x in card_list]
    for j in range(0,len(card_double_list)):
        i=card_double_list[j]
        if i>9:
            temp=0
            while i!=0:
                temp+=i%10
                i=i-temp
                i=int(i/10)
            card_double_list[j]=temp
    double_sum=sum(card_double_list)
    remaining_digits=[int(str_card_no[x]) for x in range(1,len(str_card_no),2)]
    result_sum=double_sum+sum(remaining_digits)
    return result_sum%10

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
