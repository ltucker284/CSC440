"""
This script simulates the round robin scheduling process for randomly 
generated amount of processes that have different arrival and service 
times and outputs their progress as execution time is incremented as well as
the start time, end time, initial wait time, and total wait time for each process.

Class: CSC 440
Authors: Juan Matiz, Liz Tucker
"""
from collections import deque
import random
import scheduling

# pass in any number of iterable items
def create_deque(*iterables):
    process_deque = deque()
    for process in iterables:
        for process_info in process:
            process_deque.append(process_info)
    return append_remaining_service_time_field(process_deque)

def append_remaining_service_time_field(process_deque):
    for process in process_deque:
        process.append(0)
    return process_deque

def round_robin(process_deque):
    start_time = 0
    context_switch = 0
    quantum = 2
    answer_dict = dict()
    # create a do while loop that continues until each process has been 'serviced'
    print(f"Execution Time: {start_time}", process_deque)
    while process_deque[0][3] >= 0:
        # if a process's arrival time is <= the start time, then it has 'arrived'
        if process_deque[0][2] <= start_time:
            #if a process has not been serviced yet, and it is not process zero, rotate the deque
            if process_deque[0][4] == 0:
                process_deque.rotate(-1)
                process_deque[-1][4] = 1
                continue
            # if a process id is not in answer_dict, go into this if check
            if process_deque[0][0] not in answer_dict:
                answer_dict[process_deque[0][0]] = {}
                answer_dict[process_deque[0][0]]['Start Time'] = start_time
                answer_dict[process_deque[0][0]]['Arrival Time'] = process_deque[0][2]
                answer_dict[process_deque[0][0]]['Service Time'] = process_deque[0][3]
            # if a service time is less than the assigned quantum, we don't want to waste time so pop it and start the next one
            if process_deque[0][3] < quantum and process_deque[0][3] > 0:
                print()
                print("==================SERVICE TIME LESS THAN QUANTUM======================")
                print(f"PROCESS ID: {process_deque[0][0]}, SERVICE TIME: {process_deque[0][3]}")
                print()
                start_time += process_deque[0][3]
                answer_dict[process_deque[0][0]]['End Time'] = start_time
                process_deque.popleft()
                start_time += context_switch
            # if a process has time left to fill multiple quantums, follow the regular process
            elif process_deque[0][3] >= quantum:
                process_deque[0][3] = process_deque[0][3] - quantum
                start_time += quantum
                process_deque.rotate(-1)
                start_time += context_switch
            # if the current process in the deque has service time = 0, do the stuff below
            elif process_deque[0][3] == 0:
                # add this process's end time (represented by the incremented start_time variable)
                answer_dict[process_deque[0][0]]['End Time'] = start_time
                process_deque.popleft()
                # rotate the deque so the next process get's 'serviced'
                process_deque.rotate(-1)
                start_time += context_switch
        else: 
            """
            If a process doesn't pass the 'arrival' check, rotate the deque until one that
            has arrived gets to the first position.
            
            If none have 'arrived', increment time.
            """
            entry = process_deque[0]
            while process_deque[0][2] > start_time:
                process_deque.rotate(-1)
                if process_deque[0] == entry:
                    start_time+=1
                    continue

        print(f"Execution Time: {start_time}", process_deque)
        # if there's no more items left in the deque, break the while loop
        if len(process_deque) == 0:
            break
    # return the answer dictionary
    return answer_dict

"""calculate the initial wait time of a process"""
def calculate_init_wait(arrival_time, start_time):
    return start_time - arrival_time

""" calculate the total wait time of a process """
def calculate_total_wait(end_time, service_time, arrival_time):
    return end_time - service_time - arrival_time

def main():
    list_of_processes = list(range(0,100))
    master_list = scheduling.arrival_time(list_of_processes)
    master_list = scheduling.service_time(list_of_processes, master_list)
    # create a deque of processes for round robin
    process_deque = create_deque(master_list)
    # store the answer dictionary which is the return value of the round_robin function
    answer_dict = round_robin(process_deque)
    print(f'{"PROCESS ID ":20}{"SERVICE TIME":20}{"ARRIVAL TIME ":20}{"START TIME ":20}{"END TIME ":20}{"INITIAL WAIT ":20}{"TOTAL WAIT":20}')
    # for every process in the answer dict, do the stuff below
    for entry in answer_dict:
        # get the initial wait time for each process
        answer_dict[entry]['Initial Wait Time'] = calculate_init_wait(master_list[entry][2], answer_dict[entry]['Start Time'])
        # get the total wait time of all the processes
        answer_dict[entry]['Total Wait Time'] = calculate_total_wait(answer_dict[entry]['End Time'], master_list[entry][3], master_list[entry][2])
        process_id = entry
        arrival_time = answer_dict[entry]['Arrival Time']
        service_time = answer_dict[entry]['Service Time']
        start_time = answer_dict[entry]['Start Time']
        end_time = answer_dict[entry]['End Time']
        init_wait = answer_dict[entry]['Initial Wait Time']
        total_wait = answer_dict[entry]['Total Wait Time']
        print(f'{process_id:5}{service_time:20}{arrival_time:20}{start_time:20}{end_time:20}{init_wait:20}{total_wait:20}')


if __name__ == "__main__":
    main()