"""This package takes 
"""
import pandas as pd
import fileSearch

#take in date object? or allow both?
def getDataSeries(dates, what, marketDataFolder, dataSpecific=[], source="IMDB",  DEBUG=False):

    dates = dates.map(lambda x: x.strftime("%Y%m%d")).tolist()

    
    if type(dates)  is not list: dates = [dates] #to allow user passing in just one date that is not in a list
    

    dataSeries = getDataSeriesSingle(dates.pop(), what, marketDataFolder) #make the anchor dataframe, so we can attach others to it
    
    for dt in dates:
        if(DEBUG): print dt
        dataSeries = pd.concat([dataSeries, getDataSeriesSingle(dt, what, marketDataFolder)])

    return dataSeries
    


def getDataSeriesSingle(date, what,marketDataFolder, dataSpecific=[], source="IMDB", DEBUG=False):
    '''Returns a pandas dataFrame
    Data series specific files come in a list

    ---
    getDataSeries("20140818", FX) => pd.df
    getDataSeries("20140818", FX, ['JPY']) => subset of pdf.df
    '''

    #dateStr = date.strftime("%Y%m%d")

    filePath= fileSearch.findFile2(date, what, marketDataFolder)
    if(DEBUG): "I am going to try to read in the following file", filePath

    #TODO: Make Multindex
    #dataSeries = pd.read_csv(filePath, usecols=[1,6,8,14,17], names=["Date", "Index", "Expiry", "Moneyness", "Volatility"], skipfooter=1, skiprows=1, index_col = [0])
    #print dataSeries
    arguments = "pd.read_csv(filePath," + imdbConfig[what] + ",skipfooter=1, skiprows=1, header=None)"
    dataSeries = eval(arguments)
    dataSeries = eval("dataSeries.pivot_table(" + pivotConfig[what] + ")")
    return dataSeries



#Which columns are important

imdbConfig = {
              "IDXIV": 'usecols=[1,5,8,14,17], names=["Date", "Index", "Expiry", "Moneyness", "Volatility"]',
              "FX": 'usecols = [1,5,9], names = ["Date", "Key", "ExchangeRate"]',
              "FXIV" : 'usecols = [1,5, 8, 14, 17], names = ["Date", "Key", "Expiry", "Moneyness", "Volatility"]', 
              "IRC" : 'usecols = [1,5,6,8,17], names = ["Date", "Key", "Description", "Maturity", "InterestRate"]' ,
              "IRIV" : 'usecols = [1,5,8,13,14,17], names = ["Date", "Key", "Expiry", "Tenor", "Moneyness", "Volatility"]',
              "IDX" : 'usecols = [1, 5, 6, 17], names = ["Date", "Key", "Description", "IndexLevel"]',
              "LP" : 'usecols = [1,5,8,17], names = ["Date", "Key", "Maturity", "ILPLevel"]' 
              }
          
 #these two should really be in one structure            
 #Should have been consistent with " and ' 
pivotConfig = {
               "IDXIV" : "rows = ['Date','Expiry', 'Moneyness'], values = 'Volatility', cols=['Index']",
               "FX" : "rows = ['Date'], values = 'ExchangeRate', cols=['Key']", 
               "FXIV" : "rows = ['Date','Expiry', 'Moneyness'], values = 'Volatility', cols = ['Key']",
               "IRC" : "rows = ['Date', 'Maturity'], values = 'InterestRate', cols = ['Key', 'Description']",
               "IRIV" : "rows = ['Date', 'Expiry', 'Tenor', 'Moneyness'], values = 'Volatility', cols = 'Key'", 
               "IDX" : "rows = ['Date'], values = 'IndexLevel', cols = ['Key', 'Description']",
               "LP" : "rows = ['Date', 'Maturity'], values = 'ILPLevel', cols = 'Key'"
               }

if __name__ == "__main__":

    def test_getDataSeries():
        networkMD = r"//srpzyfap0003.insim.biz/ESGShare/MD"
        getDataSeries("20140818", "IDXIV", networkMD, DEBUG = True)

    def test_getDataSeriesMany():
        networkMD = r"//srpzyfap0003.insim.biz/ESGShare/MD"
        getDataSeriesMany("20140818", "IDXIV", networkMD, DEBUG = True)

    test_getDataSeriesMany()
    test_getDataSeries()





    
    

