#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    for string in name_list:
        if string.endswith('at')and string!='at':
            count1+=1
        elif string.count('a')!=0 and (string.index('a')!=len(string)-1 and string[string.index('a')+1]=='t'):
            count2+=1
    print("_at -> ",count1)
    print("%at% -> ",count1+count2)
    
    #start writing your code here
    #Populate the variables: count1 and count2

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print("_at -> ",count1)
    #print("%at% -> ",count2)
