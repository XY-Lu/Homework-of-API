#取得10家市值最大的银行行业的上市公司从去年年初至今的股票的日行情数据，并将该数据存入MySQL数据库
'''import tushare as ts
tushare_token ='1c8b06446534ae510c8c68e38fc248b99f89ac3814cb55645ae2be72'
pro = ts.pro_api(tushare_token)
df1= pro.daily(ts_code='601398.SH,601939.SH,601288.SH,6000036.SH,601988.SH,601658.SH,601166.SH,601328.SH,000001.SZ,600000.SH',
               start_date='20200101', 
               end_date='20201113')
print(df1.head())
'''

#动量效应指的是指股票的收益率有延续原来的运动方向的趋势，即过去一段时间收益率较高的股票在未来获得的收益率仍会高于过去收益率较低的股票。
#请用调用数据去验证，如随机寻找部分的涨停股票，考察其涨停后几日的发展趋势，并和其他股票进行对比。
'''
df.loc[index, column_name],选取指定行和列的数据
df.loc[0,'id'] # 'Snow'
df.loc[0:2, ['id','title']]  # 选取第0行到第2行，id和title列的数据, 注意这里的行选取是包含下标的。
df.loc[[2,3],['id','title']]  # 选取指定的第2行和第3行，id和title列的数据
df.loc[df['webname']=='中国货币网','id']  # 选取webname列是中国货币网，id列的数据
df.loc[df['webname']=='中国货币网',['id','title']]  # 选取webname列是中国货币网，id和title列的数据
 '''
import tushare as ts
import pandas as pd 
import xlrd
import openpyxl
import json
tushare_token ='1c8b06446534ae510c8c68e38fc248b99f89ac3814cb55645ae2be72'
pro=ts.pro_api(tushare_token)
df2=pro.limit_list(trade_date='20201109', limit_type='U', fields='ts_code,close,first_time,last_time')
df3= pd.DataFrame(df2)
a=df3['ts_code'].astype("str")
df4= pro.daily(ts_code=a,
               start_date='20201110', 
               end_date='20201112') 
print(df4.head())
#df3.to_excel('C://Users//uLtra//Desktop//stock_data.xlsx')
#workbook=xlrd.open_workbook(r'C:\Users\uLtra\Desktop\stock_data.xlsx')
'''wb1=workbook.sheet_by_index(0)
code=wb1.col_values(1,1,72)
for i in code:
    code1=str(i)
    df4= pro.daily(ts_code=code1,
               start_date='20201110', 
               end_date='20201112') 
    print(df4.head())
    '''


#有人说持有低市值股票可以获利，请试试是否正确。