"""This package takes 
"""
import pandas as pd
import abc 

#do I need a abstract baseclass?

class mktDataSeries:
    """Provides an interface for raw market data
    Returns a pandas dataframe
    """
    #will be a pandas dataframe
    dataSeries = pd.DataFrame([]) 
    

class imdbDataSeries(mktDataSeries):
    
    
    def __init__(self, type):
        self.dataSeries = pd.read_csv


   
    
   

        


    
