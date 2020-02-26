import random
import sys
import time

def arrival_time(list_of_processes):
    arrival_time_dict = {}
    average_interarrival_time = 0
    for process in list_of_processes:
        interarrival_time = 4 + random.randint(4, 8)  # interarrival time is the time between successive arrivals.
        if process == list_of_processes[-1]:
            arrival_time_dict[process] = "N/A"
        else:
            arrival_time_dict[process] = interarrival_time

    for process in arrival_time_dict:
        if arrival_time_dict[process] == "N/A":
            pass
        else:
            average_interarrival_time += arrival_time_dict[process]  # Adds the current interarrival time plus the next. 

    total_processes= len(list_of_processes) - 2
    print(f"The average interarrival time is : {str(average_interarrival_time/total_processes)} ")

# def service_time(list_of_processes):
#     service_time_dict = {}
#     for process in list_of_processes:
#         service_time = 2 + random.randint(2,5)
#         pass

def main():
    list_of_processes = list(range(0,101))
    arrival_time(list_of_processes)
    # service_time(list_of_processes)
    


if __name__ == "__main__":
    main()