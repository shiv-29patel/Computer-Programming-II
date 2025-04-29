"""Write a program that creates and uses a Time class 
to perform various time arithmetic operations"""
class time:
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hour=hours
        self.minute=minutes
        self.second=seconds
        self.normalize()
    def normalize(self):
        if self.second>=60:
            extra_minute=self.second//60  
            self.second=self.second%60
            self.minute=self.minute+extra_minute  
        if self.minute>=60:
            extra_hour=self.minute//60  
            self.minute=self.minute%60
            self.hour=self.hour+extra_hour  
        if self.hour>=24:
            self.hour=self.hour%24
    def __add__(self,other):
        total_hour=self.hour+other.hour        
        total_minute=self.minute+other.minute        
        total_second=self.second+other.second
        self.normalize()
        return time(total_hour,total_minute,total_second)
    def __sub__(self,other):
        t_sec1=self.hour*3600+self.minute*60+self.second        
        t_sec2=other.hour*3600+other.minute*60+other.second
        t_sec=abs(t_sec1-t_sec2)        

        hour=t_sec//3600
        minute=(t_sec%3600)//60
        second=t_sec%60
        return time(hour,minute,second)
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

time1=time(3,45,50)
time2=time(5,12,36)

print(f"Time 1={time1}")
print(f"Time 2={time2}")

print(f"The addition is {time1+time2}")
print(f"The subtraction is {time1-time2}")