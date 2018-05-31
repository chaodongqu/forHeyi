# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import numpy as np
import pandas as pd

price_segment = [0,50,120,200,350,600]

def get_price_seg(begin , end ,sum_colum ):
    data = df[(df.Price >=begin) & (df.Price<end )] # 价格区间过滤
    data_sum =  data[sum_colum].groupby(df['Keys']).sum() #分组求和
    ret =  pd.DataFrame(data_sum)
    ret['price_seg'] = str(begin)+'_'+ str(end)
    return ret

#计算访客
df = pd.DataFrame(pd.read_excel('/Users/quchaodong/Desktop/heyi1.xlsx' 
                                ,sheet_name='visitor'
                                ,dtype = {'Price':float,'Keys':object , 'Visitors':float }
                                ,na_values=['None', ' '] ))

df_segments = []
for i in range(1 ,len(price_segment)):
    df_seg = get_price_seg(  price_segment[i -1] , price_segment[i]  ,  'Visitors')
    df_segments.append(df_seg)
    
visitor_result = pd.concat(df_segments)
print( visitor_result)

#计算订单
df = pd.DataFrame(pd.read_excel('/Users/quchaodong/Desktop/heyi1.xlsx' ,
                                sheet_name='order',
                                dtype = {'Price':float,'Keys':object , 'orders':float },
                                na_values=['None', ' '] 
                               ))
df_segments = []
for i in range(1 ,len(price_segment)):
    df_seg = get_price_seg(  price_segment[i -1] , price_segment[i]  ,  'orders')
    df_segments.append(df_seg)
    
order_result = pd.concat(df_segments)

#输出文件
with pd.ExcelWriter('/Users/quchaodong/Desktop/qucd_all_price_seg_stat.xlsx') as writer:
    visitor_result.to_excel(writer, sheet_name='visitor')
    order_result.to_excel(writer, sheet_name='order')
