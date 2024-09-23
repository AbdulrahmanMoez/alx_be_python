task = input("Enter your task: ").lower()
priority = input("priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
while True:
    match task:

        case _ if priority == "high" and time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        case _ if priority == "high" and time_bound == "no":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention as soon as possible!")
        
        
        case _ if priority == "medium" and time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires to be attention to in the next few days")
        case _ if priority == "medium" and time_bound == "no":
            print(f"Reminder: '{task}' is a medium priority task that requires to be attention to  in the nearest time")

        case _ if priority == "low" and time_bound == "yes":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _ if priority == "low" and time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _ : 
             print("We don't have any suggestion for this task")
    break
