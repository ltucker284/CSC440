import random

def arrival_time(list_of_processes):
    """This function iterates through a list of processes and appends process, interarrival time, and arrival time to a new list."""
    master_list = []
    average_interarrival_time = 0

    for process in list_of_processes:  # Iterats through a list of 100 processes.
        interarrival_time = 4 + random.randint(4,8)  # Generates an integer between 4 and 8, inclusive.
        if process == list_of_processes[0]:  # First process does not get an interarrival time either, thus it gets a zero for this value as well.
            master_list.append([process, 0])
        else:
            master_list.append([process, interarrival_time])
    
    for index in range(len(master_list)):  # Iterates through a list of indexes. 
        average_interarrival_time += master_list[index][1]  # Adds the interarrival times of each value together.
        if master_list[index][0] == 0:  # The first process executes immediatly, thus its arrival time is zero.
            master_list[index].append(0)
        else:
            arrival_time = master_list[index-1][2] + master_list[index][1]  # Grabs the arrival time of the previous process and adds the interarrival time of the current process.
            master_list[index].append(arrival_time)
    
    print(f"The Average Interarrival Time Is: {str(average_interarrival_time/len(list_of_processes))}")

    return master_list

def main():
    list_of_processes = list(range(0,100))
    master_list = arrival_time(list_of_processes)
    user_input = input("Print Process?: (y/n) ")
    while user_input != 'n':
        for index in range(len(master_list)):
            print(f"Process ID: {master_list[index][0]}, Interarrival Time: {master_list[index][1]}, Arrival Time: {master_list[index][2]}")
            user_input = input("\nPrint Next Process?: (y/n) ")
            if user_input == 'n':
                break
    print(master_list)

    # service_time(list_of_processes)
    


if __name__ == "__main__":
    main()