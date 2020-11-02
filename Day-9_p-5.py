#PF-Prac-5
def count_digits_letters(sentence):
    #start writing your code here
    res_list=[0]*2
    for i in range(0,len(sentence)):
        element=sentence[i]
        if element.isalpha()==True:
            res_list[0]+=1
        elif element.isdigit()==True:
            res_list[1]+=1
    return res_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
