import pandas as pd
import time
import datetime

def popularityMarker(NameOfFile, NameOfNewFile, number_of_days_ago, income_threshold):
    carsData = pd.read_csv(NameOfFile, encoding = 'unicode_escape')
    del carsData['Year']
    carsData['Popular'] = 'Unpopular'

    def CarsDictionary():
        brands_set = {}
        for index in range(len(carsData.index)):
            brands_set[carsData.iloc[index]['Brand']] = 0
        return brands_set

    def CarsTotalIncome(number_of_days_ago):
        CarsDctionary = CarsDictionary()
        today = datetime.date.today()
        delta = datetime.timedelta(days=number_of_days_ago)
        comparing_day = today - delta
        comparing_day_formatted = datetime.datetime.combine(comparing_day, datetime.datetime.min.time())

        for index in range(len(carsData.index)):
            if datetime.datetime.fromtimestamp(time.mktime(time.strptime(carsData['Date'][index], '%Y-%m-%d'))) > comparing_day_formatted:
                CarsDctionary[carsData.iloc[index]['Brand']] += carsData.iloc[index]['Price']

        return CarsDctionary

    def CarsIncomeFilter(income_threshold, number_of_days_ago):
        CarsIncomeDictionary = CarsTotalIncome(number_of_days_ago)
        CarsFilteredDictionary = {}
        for key in CarsIncomeDictionary:
            if CarsIncomeDictionary[key] > income_threshold:
                CarsFilteredDictionary[key] = True
        return CarsFilteredDictionary 
            
  
      
    def PopularityMarker(income_threshold):
        CarsIncomeFilteredDictionary = CarsIncomeFilter(income_threshold, number_of_days_ago)
        for key in CarsIncomeFilteredDictionary:
        #print('key')
            for index in range(len(carsData.index)):
                if carsData.iloc[index]['Brand'] == key:
                    carsData.iloc[index, 9] = 'Popular'  #ChangedCarsData.iloc[index] ['Popular'] = 'Popular'
                #print(carsData.iloc[index]['Popular'])           
        return carsData
    
    carsDataMarked = PopularityMarker(income_threshold)
    return carsDataMarked.to_csv(NameOfNewFile + '_thrashold = {}.csv'.format(income_threshold), index=False)
        


popularityMarker('Car_Data_Changed.csv', 'Car_Data', 30, 10000000)

 


