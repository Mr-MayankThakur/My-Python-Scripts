"""
Shortest Remaining Time First Scheduler

process format:
python dict{
    'name':str
    'burst_time':int
    'arrival_time':int
    'remaining_time':int
}
"""

def sort_by(processes, key, reverse=False):
    """
    sorts the given processes list according to the key specified
    """
    return sorted(processes, key=lambda process: process[key], reverse=reverse)


def available_processes(processes, time):
    """
    returns python filter object which filters the processes that have arrived according to current time and have left some remaining time
    """
    return filter(lambda x: ((x['arrival_time'] <= time) and (x['remaining_time'] > 0)), processes)


def total_of(processes, key):
    return sum([item[key] for item in processes])


def update_process(processes, name, key, new_value):
    list(filter(lambda x: x['name'] == name, processes))[0][key] += new_value


def srtf_preemptive(processes):
    total_burst_time = total_of(processes, 'burst_time')
    log = []
    for time in range(total_burst_time):
        ready_processes = available_processes(processes, time)
        shortest_job = sort_by(ready_processes, 'remaining_time')[0]
        log.append(shortest_job['name'])
        update_process(processes, shortest_job['name'], 'remaining_time', -1)
    return processes, log


if __name__ == '__main__':
    num_processes = int(input("enter total number of processes: "))
    processes = []
    for i in range(num_processes):
        print("Enter info for process {}: (in space seperated form) ".format(i))
        burst_time, arrival_time = list(map(int, input("Burst time, Arrival time = ").split()))
        processes.append({
            'name':'p{}'.format(i),
            'burst_time':burst_time,
            'arrival_time':arrival_time,
            'remaining_time':burst_time
        })

    output, log = srtf_preemptive(processes)
    print(log)