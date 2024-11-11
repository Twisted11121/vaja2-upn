from datetime import datetime, timedelta, timezone
import pytz

def birthday():
    format1 = "%d.%m.%Y"
    #user_birthday = input("Your birthday: ")
    user_birthday = "11.03.2006"
    birthdate = datetime.strptime(user_birthday, format1)
    time_today = datetime.today()
    
    seconds = round((time_today - birthdate).total_seconds(),2)
    print(f"You have been alive for {seconds} seconds!")
    
    minutes = round((time_today - birthdate).total_seconds()/60,2)
    print(f"You have been alive for {minutes} minutes!")
    
    hours = round(minutes / 60, 2)
    print(f"You have been alive for {hours} hours!")
    
    days = round(hours / 24, 2)
    print(f"You have been alive for {days} days!")
    
    heart_beat_per_second = round(seconds * 1.17, 2)
    print(f"You have been alive for {heart_beat_per_second} heart beats!")
    
    blinks_per_minute = round(((time_today - birthdate).total_seconds()/60)* 14,2)
    print(f"You have been alive for {blinks_per_minute} eye blinks!")
    
    seasons = round((days / 365) * 4, 0)
    print(f"You have seen {seasons} seasons throug out your life!")


def next_birthday():
    curr_year = datetime.now().year
    user_birthday = "11.03" 
    user_birthday = datetime.strptime(f"{user_birthday}.{curr_year}", "%d.%m.%Y") 
    
    next_bd = (user_birthday  + timedelta(days=365)) - datetime.now()
    print(next_bd)


def pocitnice():
    curr_year = datetime.now().year
    dict_pocitnice = {"oktoberskih":"28.10", "novoletnih" : "25.12", "zimskih" : "24.2", "prvo-majskih" : "28.4", "poletnih" : "25.6"}
    for x in dict_pocitnice:
        date_pocitnice = datetime.strptime(f"{dict_pocitnice[x]}.{curr_year}", "%d.%m.%Y")
        
        if date_pocitnice < datetime.now():
            date_pocitnice = date_pocitnice.replace(year=curr_year + 1)
            
        time_befor_pocitnice = date_pocitnice - datetime.now()
        print(f"\nDni do {x} pocitnic je {time_befor_pocitnice.days} dni in bodo leta {date_pocitnice.year}")


def friday_thirteenth(year_start=2024, year_stop=2030):
    dict1 = {}
    for y in range(year_stop - year_start + 1):
        for m in range(1,12+1):
            date_friday = datetime(year_start + y, m, 13)
            if date_friday.weekday() == 4:
                dict1[y+1] = date_friday.strftime('%d.%m.%Y')
                #print(f"Petek trinajsti bo: {date_friday.strftime('%d.%m.%Y')}")
            else:
                pass
    print(dict1)
    

def weekend_work_days(start="11.11.2024", stop="24.12.2024"):
    
    start = datetime.strptime(start, '%d.%m.%Y')
    stop = datetime.strptime(stop, '%d.%m.%Y')
    
    work = [0,1,2,3,4]
    
    workDays = 0
    weekendDays = 0
    
    difference = stop - start
    for x in range (difference.days):
        if (start + timedelta(days=x)).weekday() in work:
            workDays += 1
        else:
            weekendDays += 1
    
    print(workDays, weekendDays)
    

def closes_timezones(time=16):
    
    for timeZone in pytz.all_timezones:
        now = datetime.now(pytz.timezone(timeZone))
        hour = now.hour
        if hour == time:
            print(timeZone)
    
    


def main():
    #birthday()
    #next_birthday()
    #pocitnice()
    #friday_thirteenth()
    #weekend_work_days()
    closes_timezones()

if __name__ == "__main__":
    main()
