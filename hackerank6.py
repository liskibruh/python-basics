def timeConversion(s):
    # Write your code here
    time_in_12 = s
    split_time=time_in_12.split(':')
    if time_in_12.endswith('PM') and int(split_time[0])!=12:
        new_hour = int(split_time[0])
        new_hour = new_hour+12
        new_hour = str(new_hour)
        new_minute = split_time[1]
        new_second = split_time[2]
    elif time_in_12.endswith('PM') and int(split_time[0])==12:
        new_hour=split_time[0]
        new_minute = split_time[1]
        new_second = split_time[2]       

    elif time_in_12.endswith('AM') and int(split_time[0])!=12:
        new_hour=split_time[0]
        new_minute = split_time[1]
        new_second = split_time[2]

    elif int(split_time[0])==12 and time_in_12.endswith('AM'):
        new_hour=str(0)
        new_minute = split_time[1]
        new_second = split_time[2]

    time_in_24=new_hour+':'+new_minute+':'+new_second
    if time_in_24.endswith('PM'):
        time_in_24=time_in_24.replace('PM','')
    elif time_in_24.endswith('AM'):
        time_in_24=time_in_24.replace('AM','')

    return time_in_24


print(timeConversion('12:00:00PM'))