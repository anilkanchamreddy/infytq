#PF-Assgn-57
def check_prime(number):
    #remove pass and write your logic here. if the number is prime return true, else return false
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count+=1
    if count==2:
        #print(number,count)
        return True
    else:
        return False

def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
	new_num=str(num)
	temp_num=new_num
	status=True
	for i in range(1,len(new_num)+1):
	    temp_num=temp_num[1:]+temp_num[0]
	    if check_prime(int(temp_num))==True:
	        continue
	    else:
	        status=False
	        break
	#print(num,status)
	return status
	 

def get_circular_prime_count(limit):
    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    count=0
    for i in range(2,limit+1):
        if rotations(i)==True:
            #print(i,end=' ')
            count+=1
    return count

#Provide different values for limit and test your program
print(get_circular_prime_count(100))
