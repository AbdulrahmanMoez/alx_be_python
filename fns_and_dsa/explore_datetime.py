from datetime import datetime, timedelta

def display_current_datetime():
    global current_date
    current_date = datetime.now().replace(microsecond=0)
    print (f"Current date and time: {current_date}")
    return
display_current_datetime()
user_dt = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date  = timedelta(user_dt)

    print(f"Future date: {future_date + current_date.date()}")
    
calculate_future_date()
