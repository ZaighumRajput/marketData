'''This module assists in finding the right file
'''
import os, re

def findFile(marketDataFolder, date, what, source="IMDB"):
     '''Get "what" from which data

     ----
     findFile(md, "20140818", "FXIV")
     '''
     pattern = filePattern(date, what)
     #print pattern
     regex = re.compile(pattern + "*")
     matches = []
     for root, dirs, files in os.walk(marketDataFolder):
         for f in files:
            #print f
            if regex.match(f):
                matches.append(f)
     return matches[0]

def findFile2(date, what, marketDataFolder,source="IMDB", DEBUG=False):
    if(DEBUG): print "I am searching in", marketDataFolder, "for", what, "at date", date 
    #the pattern will depend on source; need to change
    pattern = filePattern(date, what)
    fileName = re.compile(pattern + "*")
    dirName = re.compile(date + "$")
    #os.listdir(marketDataFolder)

    for directory in os.listdir(marketDataFolder):
        #print directory
        if dirName.match(directory):
            
            if(DEBUG): print "I found the directory", directory
            marketDataDirectory = os.path.join(marketDataFolder, directory)
             
            for files in os.listdir(marketDataDirectory):
                #print files

                if fileName.match(files):
                    if(DEBUG):
                        print "The file that matches is", files
                        print "The full path is", os.path.join(marketDataDirectory, files)
                    return os.path.join(marketDataDirectory, files)
    
def filePattern(date, what, type = "IMDB"):
    if type == "IMDB":
        return "IMDB_" + date + "_MD" + what + "_R_"
    
if __name__ == "__main__":




    #change date
    def test_correctFile(marketDataFolder,date, what ):
        '''See if it find the correct file
        '''
        #print marketDataFolder
        print findFile2(marketDataFolder,date, what)  
        #print findFile(marketDataFolder,date, what)


    def test_newestFile(marketDataFolder, date, what):
        '''If they are duplicate finds 
        it should return the newest one
        '''

    def test_filePattern():
        assert filePattern("20140818", "IDXIV", "IMDB") == "IMDB_20140818_MDIDXIV_R_"


    currentFolder = os.path.dirname(__file__)
    MD = os.path.join(currentFolder, "fileSearchTest", "MD")
    networkMD = r"//srpzyfap0003.insim.biz/ESGShare/MD"

    
    
    #use nose to run later
    test_correctFile("20140818", "FX", networkMD) 
    #test_correctFile(MD, "20140814", "FX")

    test_filePattern()



IMDBnames = {   
                'IRC'   : 'Interest Rates',
                'IRIV'  : 'Interest Rate Implied Vol',
                'FX'    : 'Foreign Exchange Rates',
                'FXIV'  : 'Foreign Exchange Implied Vol',
                'IDX'   : 'Equity Index Levels',
                'IDXIV' : 'Equity Index Implied Vols',
                'LP'    : 'Liquidity Premium'
                
                }
    

