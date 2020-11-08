#PF-Prac-26
def check_occurence(string):
    #start writing your code here
    mat_count=string.count('mat')+string.count('Mat')
    jet_count=string.count('jet')+string.count('Jet')
    return mat_count==jet_count
string="Jet on the Mat but mat is too long"
print(check_occurence(string))
