"""This package takes 
"""
import pandas as pd
import fileSearch

def getDataSeries(date, what,marketDataFolder, dataSpecific=[], source="IMDB"):
    '''Returns a pandas dataFrame
    Data series specific files come in a list
    


    ---
    getDataSeries("20140818", FX) => pd.df
    getDataSeries("20140818", FX, ['JPY']) => subset of pdf.df
    '''
    fileSearch.findFile2(date, what, marketDataFolder)
       


def test_getDataSeries():
    networkMD = r"//srpzyfap0003.insim.biz/ESGShare/MD"
    print getDataSeries("20140818", "IDXIV", networkMD)

    
test_getDataSeries()

    
    

















#import abc 

##do I need a abstract baseclass?

#class mktDataSeries:
#    """Provides an interface for raw market data
#    Returns a pandas dataframe
#    """
#    #will be a pandas dataframe
#    dataSeries = pd.DataFrame([]) 
    

#class imdbDataSeries(mktDataSeries):
    
    
#    def __init__(self, type):
#        self.dataSeries = pd.read_csv


   
    
   

        


    
