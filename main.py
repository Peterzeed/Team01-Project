class main:
    print("Welcome to Process Scheduler ")
    print("Process Scheduler :\n1.FCFS\n2.SJF\n3.Preemptive Priority\n4.Non-Preemptive Priority\n5.Round Robin")
    process = int(input("Choose Process Scheduler (1/2/3/4/5): "))
    if process==1:
        print("FCFS Class")
    elif process==2:
        print("SJF")
    elif process==3:
        print("Preemptive Priority")
    elif process==4:
        print("Non-Preemptive Priority")
    elif process==5:
        print("Round Robin")
    else:
         print("Please Choose 1/2/3/4/5")
