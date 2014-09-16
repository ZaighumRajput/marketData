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
        
    dataSeries = pd.read_csv(filePath, usecols=[2,14,17], skipfooter=1, skiprows=1, header=None)
    arguments = "pd.read_csv(filePath," + imdbConfig["EQIV"] + ",skipfooter=1, skiprows=1, header=None)"
    print dataSeries
    dataSeries1 = eval(arguments)



#Which columns are important
imdbConfig = {"EQIV": "usecols=[2,14,17]"}     



if __name__ == "__main__":

    def test_getDataSeries():
        networkMD = r"//srpzyfap0003.insim.biz/ESGShare/MD"
        getDataSeries("20140818", "IDXIV", networkMD, DEBUG = True)

    
    test_getDataSeries()


    
    

