from output_module import output
from time_module import get_hours, get_date
from database import update_last_seen, get_last_seen
from datetime import date


def greet():

    previous_date = get_last_seen() #fetch previous date
    today_date = get_date()  #fetch todays date and store it to database

    update_last_seen((today_date))

    # previous_date = ""
    # today_date =""

    if previous_date == today_date:
        output(" Welcome back Sir")
    
    else:
         hour = int(get_hours().split()[0])  

         if hour >= 4 and hour < 12:
            output("Good Morning Sir") 
 
         elif hour >= 12 and hour < 16:
            output("Good Afternoon Sir")

         else:
            output("Good Evening Sir")

