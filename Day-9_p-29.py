#PF-Prac-29
def exchange_list(number_list):
    #start writing your code here
    length=int(len(number_list)/2)
    number_li=number_list[len(number_list):length-1:-1]+number_list[:length]
    return number_li
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
