from sjf import SJF
from rr import RoundRobin
from priority import Priority
from non_Priority import NonPriority
from non_sjf import Non_SJF
from fcfs import FCFS


class main:
    print("Welcome to Process Scheduler")
    conti = 'y'
    while conti == 'y' :
        print("Process Scheduler :\n1.FCFS\n2.Shortest job first\n3.Priority\n4.Round Robin")
        process = int(input("Choose Process Scheduler (1/2/3/4/5): "))

        if process==1:
            print("===FIRST COME FIRST SERVE SCHEDULLING===")
            n= int(input("Enter number of processes[1-10]: "))
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
            preem_choose = int(input("1.Non-preemptive\n2.Preempttive\nChoose(1/2) : "))
            print("=======================================")
            if(preem_choose == 1):
                print("Non-Preemptive Shortest job first")
                no_of_processes= int(input("Enter number of processes[1-10]: "))
                while no_of_processes < 1:
                    print("Try Again")
                    no_of_processes = int(input("No of Process [1-10]: "))
                    print("")
                while no_of_processes > 10:
                    print("Try Again")
                    no_of_processes = int(input("No of Process [1-10]: "))
                    print("")
                non_sjf = Non_SJF()
                non_sjf.processData(no_of_processes)
        
            if(preem_choose == 2):
                print("Preemptive Shortest job first")
                no_of_processes= int(input("Enter number of processes[1-10]: "))
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
        
        
        # elif(preem_choose != 2 or preem_choose != 1) : print("Please Choose 1 or 2")  

        elif process==3:
            print("===Priority Scheduling====")
            preem_choose = int(input("1.Preemptive\n2.Non-Preempttive\nChoose(1/2) : "))
            print("=======================================")
            if(preem_choose == 1):
                print("======Non-Preemptive Priority=======")
                no_of_processes = int(input("Enter number of processes[1-10]: "))
                while no_of_processes < 1:
                    print("Try Again")
                    no_of_processes = int(input("Number of Process [1-10]: "))
                    print("")
                while no_of_processes > 10:
                    print("Try Again")
                    no_of_processes = int(input("Number of Process [1-10]: "))
                    print("")
                priority = Priority()
                priority.processData(no_of_processes)    
        
            if(preem_choose == 2):
                print("======Non-Preemptive Priority=======")
                no_of_processes = int(input("Enter number of processes[1-10]: "))
                while no_of_processes < 1:
                    print("Try Again")
                    no_of_processes = int(input("Number of Process must be [1-10]: "))
                    print("")
                while no_of_processes > 10:
                    print("Try Again")
                    no_of_processes = int(input("Number of Process must be [1-10]: "))
                    print("")
                non_priority = NonPriority()
                non_priority.processData(no_of_processes)
    
        elif process==4:
            print("======Round Robin=======")
            no_of_processes = int(input("Enter number of processes[1-10]: "))
            while no_of_processes < 1:
                print("Try Again")
                no_of_processes = int(input("Number of Process [1-10]: "))
                print("")
            while no_of_processes > 10:
                print("Try Again")
                no_of_processes = int(input("Nuber of Process [1-10]: "))
                print("")
        
            rr = RoundRobin()
            rr.processData(no_of_processes)
    
    
        else:
            print("Please Choose 1/2/3/4/5")

        conti =str(input("Do you want to continue (y/n): "))
