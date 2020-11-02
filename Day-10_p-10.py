#PF-Prac-10
def string_both_ends(input_string):
	#start writing your code here
	result=None
	if len(input_string)<2:
	    result=-1
	else:
	    result=input_string[:2]+input_string[-2:]
	    
	return result

input_string="wc"
print(string_both_ends(input_string))
