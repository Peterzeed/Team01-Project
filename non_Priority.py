class NonPriority:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))

            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))

            priority = int(input(f"Enter Priority for Process {process_id}: "))

            print("=============================================")

            temporary.extend([process_id, 0, burst_time, priority])
           
            process_data.append(temporary)
        NonPriority.schedulingProcess(self, process_data)


    def schedulingProcess(self, process_data):
        process_data.sort(key=lambda x: x[3], reverse=True)
       
        start_time = []
        exit_time = []
        s_time = 0
        for i in range(len(process_data)):
            start_time.append(s_time)
            s_time = s_time + process_data[i][2]
            e_time = s_time
            exit_time.append(e_time)
            process_data[i].append(e_time)
        t_time = NonPriority.calculateTurnaroundTime(self, process_data)
        w_time = NonPriority.calculateWaitingTime(self, process_data)
        NonPriority.printData(self, process_data, t_time, w_time)


    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
            
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
       
        return average_turnaround_time


    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        
        return average_waiting_time


    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        process_data.sort(key=lambda x: x[0])
        
        print("Process ID | Arrival Time | Burst Time | Priority | Completion Time | Turnaround Time | Waiting Time |")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t\t")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')


# if __name__ == "__main__":
    
#     print("")
#     print("======Non-Preemptive Scheduling=======")
#     no_of_processes = int(input("Enter number of processes[1-10]: "))
#     while no_of_processes < 1:
#         print("Try Again")
#         no_of_processes = int(input("No of Process [1-10]: "))
#         print("")
#     while no_of_processes > 10:
#         print("Try Again")
#         no_of_processes = int(input("No of Process [1-10]: "))
#         print("")
#     priority = NonPriority()
#     priority.processData(no_of_processes)
