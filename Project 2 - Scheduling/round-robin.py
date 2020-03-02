from collections import deque

service_time_list = [75, 40, 25, 20, 45]
arrival_time_list = [0, 10, 10, 80, 85]

def round_robin(*iterables):
    start_time = 0
    quantum = 15
    # create a deque of itearble objects
    iterators = deque(map(iter, iterables))
    # while there's stuff in iterators, keep going
    while iterators:
        try:
            # while True essentially means forever until there's nothing left to be done in the loop
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()
    
for value in round_robin(service_time_list, arrival_time_list):
    print(value)