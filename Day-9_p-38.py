#PF-Prac-38
def build_index_grid(rows, columns):
    result_list=[]
    for i in range(0,rows):
        row_list=[]
        for j in range(0,columns):
            row_list.append(str(i)+','+str(j))
        result_list.append(row_list)
    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)
