#PF-Prac-25
def list_of_count(word_list):
    #start writing your code here
    count_list=[len(x) for x in word_list]
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))
