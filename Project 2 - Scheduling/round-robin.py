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
    return process_deque

def round_robin(process_deque):
    start_time = 0
    context_switch = 0
    quantum = 2
    answer_dict = dict()
    # create a do while loop that continues until each process has been 'serviced'
    while process_deque[0][3] >= 0:
        # if a process's arrival time is <= the start time, then it has 'arrived'
        if process_deque[0][2] <= start_time:
            if process_deque[0][3] < quantum:
                print("==================SERVICE TIME LESS THAN QUANTUM======================")
                print(process_deque[0][3])
            # if a process id is not in answer_dict, go into this if check
            if process_deque[0][0] not in answer_dict:
                # add the process id into the answer_dict
                answer_dict[process_deque[0][0]] = {}
                # add the start time of each process into the answer_dict
                answer_dict[process_deque[0][0]]['Start Time'] = start_time
            # decrement a process's service time by the quantum
            process_deque[0][3] = process_deque[0][3] - quantum
            # increment the start time by the quantum
            start_time += quantum
            # if the last process in the deque is <= 0, do the stuff below
            if process_deque[0][3] <= 0:
                # add this process's end time (represented by the incremented start_time variable)
                answer_dict[process_deque[0][0]]['End Time'] = start_time
                # pop the 'serviced' process from the deque
                process_deque.popleft()
            # rotate the deque so the next process get's 'serviced'
            process_deque.rotate(-1)
        else: 
            # if a process doesn't pass the 'arrival' check, rotate the deque until one that
            # has arrived gets to the first position
            process_deque.rotate(-1)
            start_time += quantum
        print(f"Execution Time: {start_time}", process_deque)
        # if there's no more items left in the deque, break the while loop
        if len(process_deque) == 0:
            break
    # return the answer dictionary
    return answer_dict

# calculate the initial wait time of a process
def calculate_init_wait(arrival_time, start_time):
    return start_time - arrival_time

# calculate the total wait time of a process
def calculate_total_wait(end_time, service_time, arrival_time):
    return end_time - service_time - arrival_time

def main():
    list_of_processes = list(range(0,10))
    master_list = scheduling.arrival_time(list_of_processes)
    master_list = scheduling.service_time(list_of_processes, master_list)
    # create a deque of processes for round robin
    process_deque = create_deque(master_list)
    # store the answer dictionary which is the return value of the round_robin function
    answer_dict = round_robin(process_deque)
    # for every process in the answer dict, do the stuff below
    for entry in answer_dict:
        # get the initial wait time for each process
        answer_dict[entry]['Initial Wait Time'] = calculate_init_wait(master_list[entry][2], answer_dict[entry]['Start Time'])
        # get the total wait time of all the processes
        answer_dict[entry]['Total Wait Time'] = calculate_total_wait(answer_dict[entry]['End Time'], master_list[entry][3], master_list[entry][2])
        # print the dict
        print(f"Answers: {answer_dict}")

if __name__ == "__main__":
    main()