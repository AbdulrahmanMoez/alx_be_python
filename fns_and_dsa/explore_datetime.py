from datetime import datetime, timedelta


current_date = datetime.now().replace(microsecond=0)
def display_current_datetime():
    print (f"Current date and time: {current_date}")



def calculate_future_date():
    display_current_datetime()
    user_dt = int(input("Enter the number of days to add to the current date: "))

    future_date  = timedelta(user_dt)

    print(f"Future date: {future_date + current_date}")
calculate_future_date()
