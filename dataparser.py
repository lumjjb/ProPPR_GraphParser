def parseData(filename, entryparser):
    f = open(filename)
    lines = f.readlines()
    f.close()
    datapoints = map(entryparser, lines)
    return datapoints

