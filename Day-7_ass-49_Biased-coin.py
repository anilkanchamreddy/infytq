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
