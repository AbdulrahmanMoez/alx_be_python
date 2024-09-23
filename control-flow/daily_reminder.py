task = str(input("Enter your task: "))
priority = str(input("Priority (high, medium, low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

while task:
    match (priority, time_bound):
        case ("high", "yes"):
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        case ("high", "no"):
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention as soon as possible!")
        case ("medium", "yes"):
            print(f"Reminder: '{task}' is a medium priority task that requires attention in the next few days.")
        case ("medium", "no"):
            print(f"Reminder: '{task}' is a medium priority task that requires attention in the nearest time.")
        case ("low", "yes"):
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case ("low", "no"):
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("We don't have any suggestion for this task.")
    break
