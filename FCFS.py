
def FCFS(processes):
    n = len(processes)

    # Calculate waiting time for each process
    waiting_time = [0] * n
    service_time = [0] * n
    ending_time = [0] * n
    set_arrival = [0] * n
    context_switch = 1

    # Calculate service time for each process
    processes.sort(key=lambda tup: tup[1])

    # Normalize arrival time
    temp = processes[0][1]
    for i in range(n):
        set_arrival[i] = processes[i][1] - temp

    # Calculate ending time, service time, waiting time for each process
    for i in range(n):
        if i == 0:
            service_time[i] = 0
            ending_time[i] = service_time[i] + processes[i][2]
            waiting_time[i] = service_time[i] - set_arrival[i]
        else:
            service_time[i] = ending_time[i-1] + context_switch
            ending_time[i] = service_time[i] + processes[i][2]
            waiting_time[i] = service_time[i] - set_arrival[i]

    # Calculate average waiting time
    total_waiting_time = sum(waiting_time)
    avg_waiting_time = total_waiting_time / n

    # Print results
    print("Process\tArrival time\tExecution time\tEnding time\tWaiting time\tService time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{set_arrival[i]}\t\t{processes[i][2]}\t\t{ending_time[i]}\t\t{waiting_time[i]}\t\t{service_time[i]}")

    print(f"\nAverage waiting time: {avg_waiting_time}")




# Get the list of processes from the user
number_of_process = int(input("Enter number of processes: "))
processes = []
for i in range(number_of_process):
    processes_name = input(f"Process name {i+1}: ")
    arrival_time = int(input(f"Time for arrival of process {i+1}: "))
    execution_time = int(input(f"Process execution time {i+1}: "))
    processes.append((processes_name, arrival_time, execution_time))

# Execute the FCFS algorithm
FCFS(processes)









