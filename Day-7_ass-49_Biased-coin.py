#PF-Tryout
#Start writing your code here
import random as guess_coin
def biased_coin():
    probability=0.7
    coin_dict={'Tail':0,'Head':0}
    for i in range(0,1000):
        if guess_coin.random()<=probability:
            coin_dict['Head']+=1
        else:
            coin_dict['Tail']+=1
    return coin_dict

print(biased_coin())

ass-50_encd_msg

#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    vow='aieouAEIOU'
    encd_msg=[]
    data_list=data.split()
    for index_word in range(0,len(data_list)):
        word=data_list[index_word]
        temp_word=''
        vow_cou=0
        for index_letter in range(0,len(word)):
            letter=word[index_letter]
            if letter in vow:
                vow_cou+=1
                continue
            else:
                temp_word+=letter
        if vow_cou==len(word):
            encd_msg.append(word)
        else:
            encd_msg.append(temp_word)
    return ' '.join(encd_msg)

data="I love Python"
print(sms_encoding(data))
