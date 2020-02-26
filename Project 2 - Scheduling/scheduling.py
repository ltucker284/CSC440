import random
import sys

def arrival_time(list_of_processes):
    arrival_time_dict = {}
    for process in list_of_processes:
        interarrival_time = 4 + random.randint(4, 8)  # interarrival time is the time between successive arrivals.
        if process == list_of_processes[-1]:
            arrival_time_dict[process] = "N/A"
        else:
            arrival_time_dict[process] = interarrival_time
            
    print(arrival_time_dict)

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