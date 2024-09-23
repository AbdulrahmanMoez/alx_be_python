task = input("Enter your task: ")
priority = input("priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

while task:
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention as soon as possible!")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires to be attention to in the next few days")
            else:
                print(f"Reminder: '{task}' is a medium priority task that requires to be attention to  in the nearest time")
        case "low":
            if time_bound == "yes":
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _ : 
            print("We don't have any suggestion for this task")
    break
