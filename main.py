from rr import RoundRobin
from priority import Priority
from NonPriority import NonPriority
from sjf import SJF
from fcfs import FCFS


class main:
    print("Welcome to Process Scheduler ")
    print("Process Scheduler :\n1.FCFS\n2.SJF\n3.Preemptive Priority\n4.Non-Preemptive Priority\n5.Round Robin")
    process = int(input("Choose Process Scheduler (1/2/3/4/5): "))

    if process==1:
        print("===FIRST COME FIRST SERVE SCHEDULLING===")
        n= int(input("Enter number of processes : "))
        while n < 1:
            print("Try Again")
            n = int(input("No of Process [1-10]: "))
            print("")
        while n > 10:
            print("Try Again")
            n = int(input("No of Process [1-10]: "))
            print("")

        fcfs = FCFS()
        FCFS.Calcurate(n)

        # p1.Calcurate()
    elif process==2:
        print("===Shortest job first===")
        no_of_processes= int(input("Enter number of processes : "))
        while no_of_processes < 1:
            print("Try Again")
            no_of_processes = int(input("No of Process [1-10]: "))
            print("")
        while no_of_processes > 10:
            print("Try Again")
            no_of_processes = int(input("No of Process [1-10]: "))
            print("")

        sjf = SJF()
        sjf.processData(no_of_processes)

    elif process==3:
        print("=======================================")
        print("===Priority Scheduling====")
        no_of_processes = int(input("Enter number of processes: "))
        while no_of_processes < 1:
            print("Try Again")
            no_of_processes = int(input("Number of Process must be [1-10]: "))
            print("")
        while no_of_processes > 10:
            print("Try Again")
            no_of_processes = int(input("Number of Process must be [1-10]: "))
            print("")

        priority = Priority()
        priority.processData(no_of_processes)
    
    elif process==4:
        print("")
        print("======Non-Preemptive Scheduling=======")
        no_of_processes = int(input("Enter number of processes[1-10]: "))
        while no_of_processes < 1:
            print("Try Again")
            no_of_processes = int(input("No of Process [1-10]: "))
            print("")
        while no_of_processes > 10:
            print("Try Again")
            no_of_processes = int(input("No of Process [1-10]: "))
            print("")
        Nonpriority = NonPriority()
        Nonpriority.processData(no_of_processes)
    
    elif process==5:
        no_of_processes = int(input("Enter number of processes: "))
        while no_of_processes < 1:
            print("Try Again")
            no_of_processes = int(input("No of Process [1-10]: "))
            print("")
        while no_of_processes > 10:
            print("Try Again")
            no_of_processes = int(input("No of Process [1-10]: "))
            print("")
        
        rr = RoundRobin()
        rr.processData(no_of_processes)
    
    
    else:
         print("Please Choose 1/2/3/4/5")
