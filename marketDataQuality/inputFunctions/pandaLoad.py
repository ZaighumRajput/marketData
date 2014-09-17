"""This package takes 
"""
import pandas as pd
import fileSearch

def getDataSeries(date, what,marketDataFolder, dataSpecific=[], source="IMDB", DEBUG=False):
    '''Returns a pandas dataFrame
    Data series specific files come in a list

    ---
    getDataSeries("20140818", FX) => pd.df
    getDataSeries("20140818", FX, ['JPY']) => subset of pdf.df
    '''
    filePath= fileSearch.findFile2(date, what, marketDataFolder)
    if(DEBUG): "I am going to try to read in the following file", filePath

    #TODO: Make Multindex
    #dataSeries = pd.read_csv(filePath, usecols=[1,6,8,14,17], names=["Date", "Index", "Expiry", "Moneyness", "Volatility"], skipfooter=1, skiprows=1, index_col = [0])
    #print dataSeries
    arguments = "pd.read_csv(filePath," + imdbConfig[what] + ",skipfooter=1, skiprows=1, header=None)"
    dataSeries = eval(arguments)
    return dataSeries


#Which columns are important
imdbConfig = {"IDXIV": 'usecols=[1,6,8,14,17], names=["Date", "Index", "Expiry", "Moneyness", "Volatility"], index_col = ["Date"]',
              "FX": 'usecols = [1,5,9], names = ["Date", "Key", "Exchange Rate"], index_col =["Date"]',
              "IRC" : 'usecols = [1,5,6,8,17], names = ["Date", "Key", "Description", "Maturity", "InterestRate"], index_col = ["Date"]' }     
              


if __name__ == "__main__":

    def test_getDataSeries():
        networkMD = r"//srpzyfap0003.insim.biz/ESGShare/MD"
        getDataSeries("20140818", "IDXIV", networkMD, DEBUG = True)

    
    test_getDataSeries()





    
    

