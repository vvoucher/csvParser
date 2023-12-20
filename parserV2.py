import pandas as pd
from datetime import datetime
import time
from json import loads

today = (datetime.today()).strftime("%Y_%m_%d")
path195 = "RS195Report" + today + ".csv"
path215 = "RS215Report" + today + ".csv"

# nazewnictwo stringow wzgl stacji

print(today)
print(path195)
timeTable = []
st1Table = []
resultTable = []
st1Table = []
file_name="auto1.csv"
print(file_name[0:4])
df=pd.read_csv("auto1.csv",encoding = 'unicode_escape', engine ='python')
df.columns = ['No','Date','Time','ID','Result','ST01','ST02','ST03','ST04',*df.columns[9:]] 
print(len(df.columns))
myCols=['No','Date','Time','ID','Result','ST01','ST02','ST03','ST04','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
df=df.set_axis(myCols,axis=1)
myCols2=['No','Date','Time','ID','Result','ST01','ST02','ST03','ST04']
df=df.loc[:,myCols2]
resultFilter=(df['Result'] == 'NG')
df= df.loc[resultFilter]

st1Res = df.loc[~((df['ST01'] <= 0.8) & (df['ST01'] >= 0))]
st1Res=st1Res.loc[:,('Date','Time','ST01', 'ID')]
# dateTable=st1Res['Date']
# timeTable2=st1Res['Time']
newTable= []
st1Res['FullDate']= st1Res['Date'] + ' ' + st1Res['Time']
for n in range(0,len(st1Res['Time'])):
    sum = st1Res['Date'].iloc[n] + " " + st1Res['Time'].iloc[n]
    format_date = (datetime.strptime(sum, '%Y/%m/%d %H:%M:%S')).timestamp()
    if format_date != 0:
        newTable.append(int(format_date))
        # print(format_date)

st1Data=pd.DataFrame({'timestamp': newTable})
st1Data = st1Data.set_index(st1Res.index)
st1Res['timestamp'] = st1Data.iloc[:,0].values
st1Res = st1Res.set_index(st1Res['timestamp'])
st1Res=st1Res.sort_index()
# st1Res['Time'] = st1Res['Time'].dt.hour
# st1Res['timestamp'] = pd.to_datetime(st1Res['timestamp'])
st1Res['Hour'] = pd.to_datetime(st1Res['FullDate'], format='%Y/%m/%d %H:%M:%S', exact=False)
st1Res['Hour'] = st1Res['Hour'].astype(str).str[11:13]
counts = st1Res.groupby('Hour').size()

st1Res.to_csv('st1Out.csv', index=False)
st1Data.to_csv('st1data.csv', index = False)

# st2Res.to_csv('st2Out.csv', index=False)
# st3Res.to_csv('st3Out.csv', index=False)

# print(st1Res)
# print(newTable)
# print("\n")
print(counts)