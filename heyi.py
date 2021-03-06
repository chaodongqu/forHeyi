# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import numpy as np
import pandas as pd

src_file ="heyi1.xlsx" ;
det_file="price_seg_stat.xlsx"
price_segment = [0,50,120,200,350,600]

def get_price_seg(begin , end ,sum_colum ):
    data = df[(df.Price >=begin) & (df.Price<end )] # 价格区间过滤
    data_sum =  data[sum_colum].groupby(df['Keys']).sum() #分组求和
    ret =  pd.DataFrame(data_sum)
    ret['price_seg'] =  "%04d"%begin + "_" + "%04d"%end
    return ret

#计算访客
df = pd.DataFrame(pd.read_excel(src_file 
                                ,sheet_name='visitor'
                                ,dtype = {'Price':float,'Keys':str , 'Visitors':float }
                                ,na_values=['None', ' '] ))

df_segments = []
for i in range(1 ,len(price_segment)):
    df_seg = get_price_seg(  price_segment[i -1] , price_segment[i]  ,  'Visitors')
    df_segments.append(df_seg)
    
visitor_result = pd.concat(df_segments)

visitor_result = visitor_result.sort_index()


#计算订单
df = pd.DataFrame(pd.read_excel(src_file ,
                                sheet_name='order',
                                dtype = {'Price':float,'Keys':str , 'orders':float },
                                na_values=['None', ' '] 
                               ))
df_segments = []
for i in range(1 ,len(price_segment)):
    df_seg = get_price_seg(  price_segment[i -1] , price_segment[i]  ,  'orders')
    df_segments.append(df_seg)
    
order_result = pd.concat(df_segments)
order_result = order_result.sort_index()

#输出文件

with pd.ExcelWriter(det_file) as writer:
    visitor_result.to_excel(writer, sheet_name='visitor')
    order_result.to_excel(writer, sheet_name='order')
