import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import datetime
import copy

sql1 = "SELECT * from fx where a = 'USD' or b = 'USD' and (day != 20000806 or day != 20010607) and day > 20140101  order by a, b, day limit 500000"


sql2 = "SELECT * from fx where (day != 20000806 and day != 20010607 and day != 20050507) and day > 20090301 order by a, b, day"

sqlall = "SELECT * from fx group by a, b order by a, b, day"


engine = create_engine('mysql://root:cms001@localhost/test', echo=True)
cnx = engine.raw_connection()
df = pd.read_sql(sql2, cnx)
#af = pd.read_sql(sql1, cnx)
#a_pairs = pd.read_sql(sqlall, cnx)
#print pairs




#print df

AUDUSD = df[(df.a == 'AUD') & (df.b == 'USD')]
EURUSD = df[(df.a == 'EUR') & (df.b == 'USD')]
GBPUSD = df[(df.a == 'GBP') & (df.b == 'USD')]
USDCAD = df[(df.a == 'USD') & (df.b == 'CAD')]
USDCHF = df[(df.a == 'USD') & (df.b == 'CHF')]
USDJPY = df[(df.a == 'USD') & (df.b == 'JPY')]
EURJPY = df[(df.a == 'EUR') & (df.b == 'JPY')]
AUDJPY = df[(df.a == 'AUD') & (df.b == 'JPY')]
EURGBP = df[(df.a == 'EUR') & (df.b == 'GBP')]
EURCHF = df[(df.a == 'EUR') & (df.b == 'CHF')]
GBPJPY = df[(df.a == 'GBP') & (df.b == 'JPY')]
AUDCHF = df[(df.a == 'AUD') & (df.b == 'CHF')]


upairs = [AUDUSD, EURUSD, GBPUSD, USDCAD, USDCHF, USDJPY, EURJPY, EURGBP, EURCHF, GBPJPY, AUDCHF]

opy = copy.deepcopy(upairs)

for p in upairs:
    p['day'] = [datetime.datetime.combine(datetime.date(int(str(time)[0:4]), int(str(time)[4:6]), int(str(time)[6:])), datetime.time()) for time in p['day']]
    p[['day']] = p[['day']].astype('datetime64[ns]')
    #p = p.set_index('day')
    #print p

"""
for p in a_pairs:
    p['day'] = [datetime.datetime.combine(datetime.date(int(str(time)[0:4]), int(str(time)[4:6]), int(str(time)[6:])), datetime.time()) for time in p['day']]
    p[['day']] = p[['day']].astype('datetime64[ns]')
    #p = p.set_index('day')
    print p
"""

for p in opy:
    p['day'] = [datetime.datetime.combine(datetime.date(int(str(time)[0:4]), int(str(time)[4:6]), int(str(time)[6:])), datetime.time()) for time in p['day']]
    p[['day']] = p[['day']].astype('datetime64[ns]')
    #p = p.set_index('day')
    #print p



print upairs[0].dtypes
print upairs[5].dtypes

#print upairs[1]

rows_list = []

for i in range(len(upairs) -1):
   for j in range(len(upairs)):
      if i == j: continue
      if j < i: continue
      #a_pairs[j].columns = ['day', 'av', 'x', 'y']
      opy[j].columns = ['day', 'av', 'x', 'y'] 
      join = pd.merge(upairs[i], opy[j], left_index=False, right_index=False)
      #print join.a.ix[4], join.b.ix[4]
      #print join.x.ix[4], join.y.ix[4]
      corr = join.av.corr(join.avg)
      #print corr
      try:
         dict1 = {'pair1': str(join.a.ix[52] + join.b.ix[52]), 'pair2': str(join.x.ix[52] + join.y.ix[52]), 'corr': corr}

         rows_list.append(dict1)
      except:
         continue


corrs = pd.DataFrame(rows_list)
corrs = corrs.sort(['corr'])
print corrs

corrs.to_html('pcorrs.html')

      #print join.avg.corr(join.av)

      #print join.head()



#upairs[5].columns = ['day', 'av', 'x', 'y']

#join = pd.merge(upairs[0], upairs[5], left_index=False, right_index=False)

#print join

#print join.av.corr(join.avg)
#print join.avg.corr(join.av)

