from collections import deque

process_id_list = [1, 2, 3, 4, 5]
service_time_list = [75, 40, 25, 20, 45]
arrival_time_list = [0, 10, 10, 80, 85]

# pass in any number of iterable items
def round_robin(*iterables):
    start_time = 0
    quantum = 15
    process_deque = deque()
    # create a deque of itearble objects
    print(iterables[1])
    while True:
        for time in iterables[1]:
            if time <= start_time:
                process_deque.append()



    # while there's stuff in iterators, keep going
#     while iterators:
#         try:
#             # while True essentially means forever until there's nothing left to be done in the loop
#             while True:
#                 yield next(iterators[0])
#                 iterators.rotate(-1)
#         except StopIteration:
#             # Remove an exhausted iterator.
#             iterators.popleft()
    
# for value in round_robin(arrival_time_list, service_time_list):
#     print(value)
round_robin(process_id_list, arrival_time_list, service_time_list)