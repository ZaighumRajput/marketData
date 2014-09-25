from pandas.tseries.offsets import BDay
from pandas.tseries.offsets import BusinessMonthEnd
from pandas.tseries.offsets import BusinessMonthBegin

import pandas as pd
from datetime import datetime
 

def makeListOfDates(frequency, startingDate, endDate = datetime.today()  ):  # default is 1, because you might want to just compare beginning of month
    '''
    Returns a list of dates
    '''
   
    if frequency == 'Daily':
        print "[DEBUG] I will make a list of business dates from", startingDate, "to", endDate, "with DAILY Business timesteps"
        return pd.date_range(startingDate, endDate, freq=BDay())
        # return pd.data_range(startingDate, endDate, freq=BDay())
        
#weekly
    if frequency == 'Weekly':
        print "[DEBUG] I will make a list of business dates from", startingDate, "to", endDate, "with WEEKLY timesteps"
        

    if frequency == 'Monthly_End':
        print "[DEBUG] I will make a list of business dates from", startingDate, "to", endDate, "with DAILY Business timesteps"
        return pd.date_range(startingDate, endDate, freq=BusinessMonthEnd())      

    if frequency == 'Monthly_Start':
        print "[DEBUG] I will make a list of business dates from", startingDate, "to", endDate, "with DAILY Business timesteps"
        return pd.date_range(startingDate, endDate, freq=BusinessMonthBegin())          

    


def makeListOfDates_Test():
    testRange = makeListOfDates('Daily', datetime(2014, 9, 12), datetime.today())                   
    for day in testRange:
        print day.strftime("%A, %d-%m-%Y")

def makeListOfDates_Test_Monthly_End():

    businessMonthEndDates2013 = ["Thursday, 31-01-2013",
    "Thursday, 28-02-2013",
    "Friday, 29-03-2013",
    "Tuesday, 30-04-2013",
    "Friday, 31-05-2013",
    "Friday, 28-06-2013",
    "Wednesday, 31-07-2013",
    "Friday, 30-08-2013",
    "Monday, 30-09-2013",
    "Thursday, 31-10-2013",
    "Friday, 29-11-2013",
    "Tuesday, 31-12-2013"]

    testRange = makeListOfDates('Monthly_End', datetime(2013, 1, 1), datetime(2014,1,1)) 
    #print testRange.count()                
    for i in range(0,len(testRange)):
        if(DEBUG):
            print testRange[i]
            print businessMonthEndDates2013[i]
        assert testRange[i].strftime(("%A, %d-%m-%Y") == BusinessMonthEndDates[i]

