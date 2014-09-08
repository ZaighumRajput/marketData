import os, re

def findfile(filepattern, base = '.'):
    regex = re.compile(filepattern)
    matches = []
    for root, dirs, files in os.walk(base):
        for f in files:
            if regex.match(f):
                matches.append(f)
            return matches

print findfile("IMDB*C://Git//marketDataQuality//marketDataQuality//fileSearchTest//MD")