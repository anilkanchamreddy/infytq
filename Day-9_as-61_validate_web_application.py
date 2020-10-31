#PF-Assgn-61
import re
def validate_name(name):
    #Start writing your code here
    if len(name)<=15 and name.isalpha()==True:
        return True
    return False

def validate_phone_no(phno):
    #Start writing your code here
    phon_set=set(phno)
    if (len(phon_set)!=1 and phno.isdigit()==True) and len(phno)==10:
        return True
    else:
        return False


def validate_email_id(email_id):
    #Start writing your code here
    status=False
    check_list=['@gmail.com','@yahoo.com','@hotmail.com']
    sp_chr_cou=email_id.count('@')
    com_chr_cou=email_id.count('.com')
    for i in check_list:
        if email_id.endswith(i)and(sp_chr_cou==1 and com_chr_cou==1):
            status=True
    return status

def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")
    if validate_name(name)!=True:
        print("Invalid Name")
    elif validate_phone_no(phone_no)!=True:
        print("Invalid phone number")
    elif validate_email_id(email_id)!=True:
        print("Invalid email id")
    else:
        print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
