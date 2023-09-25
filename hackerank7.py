    def timeConversion(s):
        # Write your code here
        time = s
        split_time=time.split(':')

        if time.endswith('PM') and split_time[0]!='12':
            new_hour=int(split_time[0])+12
        elif time.endswith('PM') and split_time[0]=='12':
            new_hour=str(12)

        if time.endswith('AM') and split_time[0]!='12':
            new_hour=int(split_time[0])
        elif time.endswith('AM') and split_time[0]=='12':
            new_hour=str(00)

        new_hour=str(new_hour)
        new_hour =new_hour.zfill(2)
        time_in_24=new_hour+':'+split_time[1]+':'+split_time[2]

        if time_in_24.endswith('AM'):
            time_in_24=time_in_24.replace('AM','')
        elif time_in_24.endswith('PM'):
            time_in_24=time_in_24.replace('PM','')

        return time_in_24


print(timeConversion('01:00:00AM'))