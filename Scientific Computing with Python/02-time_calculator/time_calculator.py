"""
Write a function named add_time that takes in two required parameters and one optional parameter:
a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.
If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.
"""
from datetime import date, datetime,timedelta
import calendar


def add_time(start, duration,startDay = ""):
    start_format_str = '%I:%M %p'
    duration_format_str = '%H:%M'
         
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])
     
    given_time = datetime.strptime(start, start_format_str)
    if startDay != "":
        start_day = dict(zip(calendar.day_name,range(1,8)))[startDay.lower().capitalize()] 
        given_time = given_time.replace(day=start_day)
    
    new_time = given_time + timedelta(hours=duration_hours, minutes=duration_minutes)
    new_time_var = new_time
    new_time = new_time.strftime('%I:%M %p')
    if new_time[0] == "0":
        new_time = new_time[1:]

    if (startDay != ""):
        new_time += ", " + calendar.day_name[new_time_var.weekday()]
        
    if given_time.day != new_time_var.day:
        n = new_time_var.day - given_time.day
        if (n == 1):
            new_time = new_time + " (next day)"
        else:
            new_time = new_time + f" ({n} days later)"
    return new_time



#actual = add_time("3:30 PM", "2:12", "Monday")
#expected = "5:42 PM"
#print(f"expected: {expected}, actual: {actual}")