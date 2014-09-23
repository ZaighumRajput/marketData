from pandas.tseries.offsets import BDay
from pandas.tseries.offsets import BusinessMonthBegin

import pandas as pd
from datetime import datetime
#def changes(starting, end):
 


 

def makeListOfDates(frequency, startingDate, endDate = datetime.today()  ):  # default is 1, because you might want to just compare beginning of month
    '''
    Returns a list of dates
    '''
   
    if frequency == 'D':
        print "[DEBUG] I will make a list of business dates from", startingDate, "to", endDate, "with DAILY Business timesteps"
        return pd.date_range(startingDate, datetime.today(), freq=BDay())
        # return pd.data_range(startingDate, endDate, freq=BDay())
        

    if frequency == 'W':
        print "[DEBUG] I will make a list of business dates from", startingDate, "to", endDate, "with WEEKLY timesteps"
        
        



        #while(numberOfDaysInBetween > 0):
        #    print numberOfDaysInBetween
        #    numberOfDaysInBetween -= 1

        

    


def makeListOfDates_Test():
    testRange = makeListOfDates('D', datetime(2014, 9, 12), datetime.today())
    for day in testRange:
        print day.strftime("%A, %d-%m-%Y")

makeListOfDates_Test()
