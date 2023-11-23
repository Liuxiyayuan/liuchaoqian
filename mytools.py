import pandas as pd
from pyreadstat import pyreadstat
def 有序类别变量描述统计表(文件路径, 变量):
    数据表变量及文件名 = 文件路径 
    数据表,metadata = pyreadstat.read_sav(F'data\identity.sav',apply_value_formats=True,formats_as_ordered_category=True)
    count = 0
    df_result = pd.DataFrame(数据表[变量]).value_counts(sort=False)
    df_result['累计求和'] = df_result[count].cumsum()
    df_result['比例'] = 数据表[变量].value_counts(normalize=True)
    df_result['累计比例'] = df_result['比例'].cumsum()
__all__ = ['有序类别变量描述统计表']


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
def 绘制直方图(df2):  
    x = df2.index  
    count = 0
    y = df2['年级']  
    fig, ax2 = plt.subplots() 
__all__ = ['绘制直方图']