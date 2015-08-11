__author__ = 'p.bornikoel'
from client import Client
from distance_matrix import distance_matrix
import asyncio
import datetime
try: # Python 3
    from urllib.parse import urlencode
except ImportError: # Python 2
    from urllib import urlencode

print (datetime.datetime.now())
@asyncio.coroutine
def extract(client_key,origins,destinations,time):
    Google= Client(client_key)
    tasks=[]
    results=[]
    for t in time:
        tasks.append(distance_matrix(Google,origins,destinations,departure_time=t))
    for task in asyncio.as_completed(tasks):
        matrix = yield from task
        results.append(matrix)
        #matrix= yield from distance_matrix(Google,origins,destinations,departure_time=time)

    return results


key="AIzaSyCtno63LWSOFH8LDioRDUlyjXjzAFr4gjY"
o=["Arnulfstrasse+27+Muenchen","Molkereiweg+3+Piesenkam","d'epernay+42+reims"]
d=["Clemensstrasse+2+Muenchen","Arnulfstrasse+27+Muenchen","Molkereiweg+3+Piesenkam","d'epernay+42+reims"]
loop = asyncio.get_event_loop()
times=[]
for i in range(0,10):
    times.append(datetime.datetime(2015,8,11,8) + datetime.timedelta(hours=i))
results = loop.run_until_complete(extract(key,o,d,times))
for matrix in results:
    print (matrix)
    print (matrix[u'destination_addresses'])
    i=0
    for x in (matrix[u'rows']):
        d=[]
        for z in x[u'elements']:
            d.append(z[u'duration'][u'value'])

        print (matrix[u'origin_addresses'][i], d)
        i += 1
