#PF-Assgn-55

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count=0
    for i in ticket_list:
        temp_ticket=i.split(':')
        if temp_ticket[-2]==destination:
            count+=1
    return count
    #Remove pass and write your logic here

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    temp_fl_no=[]
    result=[]
    for i in ticket_list:
        temp_list=i.split(':')
        temp_fl_no.append(temp_list[0])
    temp_fl=set(temp_fl_no)
    for i in temp_fl:
        count=0
        for j in temp_fl_no:
            if i==j:
                count+=1
        result.append(i+':'+str(count))
    return result
    #Remove pass and write your logic here

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    passenger_list=find_passengers_per_flight()
    temp_dict={}
    pass_cou_list=[]
    result_pass=[]
    for i in passenger_list:
        temp_list=i.split(':')
        temp_dict[temp_list[1]]=temp_list[0]
        pass_cou_list.append(int(temp_list[1]))
    pass_cou_list.sort(reverse=True)
    for i in pass_cou_list:
        result_pass.append(temp_dict[str(i)]+':'+str(i))
    return result_pass
        
    #Remove pass and write your logic here

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())
