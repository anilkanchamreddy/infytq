#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    new_sentence=[]
    sentence_list=sentence.split()
    for index in range(0,len(sentence_list)):
        temp_word_vow=''
        temp_word_con=''
        temp_word=0
        temp_word=sentence_list[index]
        if index%2==0 or index==0:
            new_sentence.append(temp_word[::-1])
        else:
            for element in temp_word:
                if element in 'aeiouAEIOU':
                    temp_word_vow += element
                else:
                    temp_word_con += element
            new_sentence.append(temp_word_con+temp_word_vow)
    return ' '.join(new_sentence)
    
    sentence='The sun rises in the east'
    print(encrypt_sentence())
