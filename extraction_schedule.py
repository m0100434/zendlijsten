# import packages 

#import schedule
import time
from datetime import date, timedelta


# wake up 

# 3. start the iteration

def job:
    for i in range (-20,3):
        date = date.today() + timedelta(days=i)
        day = date.strftime("%d")
        month = date.strftime("%m")
        combo = day+"-"+month+"-2021"
        print(date, "equals", combo)

## 3.1. check if the file exists

## IF NO

### 3.2 execute 'main_extraction'

%main_extraction(day= ,month= )

## IF YES
#next iteration

#end loop


# 6. if end is achieved, then goto sleep for 12 hours


schedule.every().day.at("11:00").do(job,'It is 11:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute

