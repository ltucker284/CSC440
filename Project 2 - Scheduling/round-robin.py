from collections import deque

# pass in any number of iterable items
def round_robin(*iterables):
    start_time = 0
    quantum = 15
    process_deque = deque()
    answer_dict = dict()
    for item in iterables:
        for item in item:
            process_deque.append(item)
    while process_deque[0][2] > 0:
        if process_deque[0][1] <= start_time:
            if process_deque[0][0] not in answer_dict:
                answer_dict[process_deque[0][0]] = start_time
                print(answer_dict)

            process_deque[0][2] = process_deque[0][2] - quantum
            start_time += quantum
            if process_deque[-1][-1] <= 0:
                process_deque.pop()
            process_deque.rotate(-1)
        else: 
            process_deque.rotate(-1)
        print(f"Execution Time: {start_time}", process_deque)
        if len(process_deque) == 0:
            break
    return answer_dict


def main():
    process_list = [[1,0,75],[2,10,40],[3,10,25],[4, 80,20],[5,85,45]]
    process_dict = {
        1:{
            "Service Time":75,
            "Arrival Time":0
        },
        2:{
            "Service Time":40,
            "Arrival Time":10
        },
        3:{
            "Service Time":25,
            "Arrival Time":10
        },
        4:{
            "Service Time":20,
            "Arrival Time":80
        },
        5:{
            "Service Time":45,
            "Arrival Time":85
        }
    }

    print(round_robin(process_list))

if __name__ == "__main__":
    main()