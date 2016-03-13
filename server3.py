import fk_db

cache={}

def print_name():
    return str(__name__)


def updateLastCountSq(a,b,result):
    key='lastFive'
    lastFiveList=cache.get(key)
    if lastFiveList:
        if len(lastFiveList)>=5:
            newList=lastFiveList[1:]
            newList.append("{} * {}={}".format(a,b,result))
            cache[key]=newList

        else:
            lastFiveList.append("{} * {}={}".format(a,b,result))
            cache[key]=lastFiveList

    else:
        cache[key]=["{} * {}={}".format(a,b,result)]


def lastCountSqHandler():
    key='lastFive'
    if key in cache:
        return "Last 5 Results = {}".format(cache[key])
    else:
        return "Combination not used before"
       
       
def CountSqHandler(a,b):
    cachekey=(a,b)
    if cachekey in cache:
        return cache[cachekey]
    else:
        result=fk_db.count_sq(a,b)
        updateLastCountSq(a,b,result)
        cache[cachekey]=result
        return 'Total Number of square are:{}'.format(result)
        lastCountSqHandler()

if __name__ == '__main__':
    CountSqHandler(2,6)
    CountSqHandler(5,6)
    CountSqHandler(10,6)
    CountSqHandler(3,6)
    CountSqHandler(4,6)
    CountSqHandler(11,6)
    CountSqHandler(20,16)

    
