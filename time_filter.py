import pandas as pd
import time
import datetime

carsData = pd.read_csv('Car_Data_Changed.csv', encoding = 'unicode_escape')

#print(type(carsData['Date'][0]))

def cars_data_filtered_by_time(number_of_days_ago):
    today = datetime.date.today()
    delta = datetime.timedelta(days=number_of_days_ago)
    comparing_day = today - delta
    day = datetime.datetime.combine(comparing_day, datetime.datetime.min.time())
    #print(type(datetime.datetime.fromtimestamp(time.mktime(time.strptime(carsData['Date'][0], '%Y-%m-%d')))))
    #print(datetime.datetime.fromtimestamp(time.mktime(time.strptime(carsData['Date'][10], '%Y-%m-%d'))) > day)

    cars_data_filterred_by_time = carsData.loc[datetime.datetime.fromtimestamp(time.mktime(time.strptime(carsData['Date'], '%Y-%m-%d'))) > day]
    return cars_data_filterred_by_time

print(cars_data_filtered_by_time(15))
#datetime.datetime.fromtimestamp(time.mktime(struct))