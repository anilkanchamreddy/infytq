#PF-Prac-8
def calculate_net_amount(trans_list):
    #start writing your code here
    net_amount=0
    for i in range(0,len(trans_list)):
        if trans_list[i][0]=='D':
            net_amount+=int(trans_list[i][2:])
        elif trans_list[i][0]=='W':
            net_amount-=int(trans_list[i][2:])
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
