"""
This script simulates the scheduling process of a list of 100 processes and 
calculates interarrival time, arrival time, average interarrival time, and
average service time.

Class: CSC 440
Authors: Juan Matiz, Liz Tucker
"""
import random

def arrival_time(list_of_processes):
    """This function iterates through a list of processes and appends process, interarrival time, and arrival time to a new list."""
    master_list = []
    interarrival_time = 0

    for process in list_of_processes:  # Iterates through a list of 100 processes.
        interarrival_time = random.randint(2,6)  # Generates an integer between 2 and 6, inclusive.
        if process == list_of_processes[0]:  # First process does not get an interarrival time, thus it gets a zero for this value.
            master_list.append([process, 0])
        else:
            master_list.append([process, interarrival_time])
    
    for index in range(len(master_list)):  # Iterates through a list of indexes. 
        interarrival_time += master_list[index][1]  # Adds the interarrival times of each value together.
        if master_list[index][0] == 0:  # The first process executes immediatly, thus its arrival time is zero.
            master_list[index].append(0)
        else:
            arrival_time = master_list[index-1][2] + master_list[index][1]  # Grabs the arrival time of the previous process and adds the interarrival time of the current process.
            master_list[index].append(arrival_time)
    
    print(f"The average interarrival time is: {str(interarrival_time/len(list_of_processes))}")

    return master_list

def service_time(list_of_processes, master_list):
    """This function iteratess through a list of processes, creates a dictionary with the process id as the key, and assigns the service time as the value for each key."""
    service_time_dict = {}
    average_service_time = 0
    for process in list_of_processes:  # Iterates through a list of 100 processes.
        service_time = random.randint(2,5)  # Generates an integer between 2 and 5, inclusive.
        service_time_dict[process] = service_time
        master_list[process].append(service_time)

    for time in service_time_dict:
        average_service_time += service_time_dict[time]
    print(f"\nThe average service time is : {str(average_service_time/len(list_of_processes))}")
    print()
    return master_list

# def create_dictinary(master_list):
#     process_dict = {}
#     for process in master_list:
#         process_dict[f"Process ID: {str(process[0])}"]["Interarrival Time"] = process[1]
#         process_dict[f"Process ID: {str(process[0])}"]["Arrival Time"] = process[2]
#         process_dict[f"Process ID: {str(process[0])}"]["Service Time"] = process[3]
    
#     print(process_dict)


def main():
    """This process handles the script logic"""
    list_of_processes = list(range(0,1000))
    master_list = arrival_time(list_of_processes)
    
    user_input = input("Print Process?: (y/n) ")
    while user_input != 'n':
        for index in range(len(master_list)):
            print(f"Process ID: {master_list[index][0]}, Interarrival Time: {master_list[index][1]}, Arrival Time: {master_list[index][2]}")
            user_input = input("\nPrint Next Process?: (y/n) ")
            if user_input == 'n':
                break

    master_list = service_time(list_of_processes, master_list)
    print(master_list)
    # create_dictinary(master_list)
    


if __name__ == "__main__":
    main()