#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
data = pd.read_csv(r"C:\Users\34367\Desktop\新零售-前置知识数据及代码\项目数据\附件1.csv",encoding="gbk")
data = data.drop([70679])
data['支付时间'] = pd.to_datetime(data['支付时间'])
order_A = data.loc[data['地点'] == 'A',:]
order_B = data.loc[data['地点'] == 'B',:]
order_C = data.loc[data['地点'] == 'C',:]
order_D = data.loc[data['地点'] == 'D',:]
order_E = data.loc[data['地点'] == 'E',:]
order_A.to_csv("task1-1A.csv",encoding="gbk")
order_B.to_csv("task1-1B.csv",encoding="gbk")
order_C.to_csv("task1-1C.csv",encoding="gbk")
order_D.to_csv("task1-1D.csv",encoding="gbk")
order_E.to_csv("task1-1E.csv",encoding="gbk")


# In[2]:



def task2(position,month):
    data2 = pd.read_csv(r""+position,encoding = 'gbk')
    data2_month = pd.to_datetime(data2['支付时间']).dt.month
    data2_2 = data2.loc[data2_month == month]
    data2_money = data2_2['实际金额'].sum()
    data2_sell = data2_2['商品'].size
    print('交易额：'+ str(data2_money) + ' 订单量为： ' + str(data2_sell))
task2('task1-1A.csv',5)
task2('task1-1B.csv',5)
task2('task1-1C.csv',5)
task2('task1-1D.csv',5)
task2('task1-1E.csv',5)


# In[5]:


def task3(position,month):
    data2 = pd.read_csv(r""+position,encoding = 'gbk')
    data2_month = pd.to_datetime(data2['支付时间']).dt.month
    data2_2 = data2.loc[data2_month == month]
    data2_money = data2_2['实际金额'].sum()
    data2_sell = data2_2['商品'].size
    moneyAverage = data2_money/data2_sell
    print("%.2f" % moneyAverage,end = " ")
def task1_3_2(position,month):
    data2 = pd.read_csv(r""+position,encoding = 'gbk')
    data2_month = pd.to_datetime(data2['支付时间']).dt.month
    data2_2 = data2.loc[data2_month == month]
    data2_sell = data2_2['商品'].size
    return data2_sell
for i in range(12):
    task3('task1-1A.csv',i + 1) 
    task3('task1-1B.csv',i + 1) 
    task3('task1-1C.csv',i + 1) 
    task3('task1-1D.csv',i + 1) 
    task3('task1-1E.csv',i + 1) 
    print()
    


# In[6]:


def task1_3_2(position,month):
   data2 = pd.read_csv(r""+position,encoding = 'gbk')
   data2_month = pd.to_datetime(data2['支付时间']).dt.month
   data2_2 = data2.loc[data2_month == month]
   data2_sell = data2_2['商品'].size
   return data2_sell
def task1_3_2_2(position):
   for i in range(12):
       month = [31,28,31,30,31,30,31,31,30,31,30,31]
       sumSell = task1_3_2(r"" + position,i + 1)
       averageSell = sumSell / month[i]
       print("%.2f" % averageSell)
task1_3_2_2("task1-1A.csv")
task1_3_2_2("task1-1B.csv")
task1_3_2_2("task1-1C.csv")
task1_3_2_2("task1-1D.csv")
task1_3_2_2("task1-1E.csv")


# In[7]:


import numpy as np
import pandas as pd
data = pd.read_csv(r"C:\Users\34367\Desktop\新零售-前置知识数据及代码\项目数据\附件1.csv",encoding="gbk")
data = data.drop([70679])
data['支付时间'] = pd.to_datetime(data['支付时间'])
data_month = pd.to_datetime(data['支付时间']).dt.month
task2_1 = data.loc[data_month == 6,:]
task2_1Group = task2_1.groupby(by = '商品')
print(task2_1Group.count().sort_values(by = '订单号',ascending = False))


# In[9]:


import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('商品')
plt.ylabel('销量')
commodity = ['怡宝纯净水','40g双汇\n玉米热狗肠','东鹏特饮','脉动','250ml维他柠檬茶']
sell = [657,240,238,235,225]
for i in range(5):
    plt.bar(commodity[i],sell[i],width=0.5)
for i in range(5):
    plt.text(i, sell[i], sell[i], va='bottom', ha='center')
plt.title("2017年6月销量前五的商品销量")
plt.show()


# In[16]:


def task2_2(position,month):
    data2 = pd.read_csv(r""+position,encoding = 'gbk')
    data2_month = pd.to_datetime(data2['支付时间']).dt.month
    data2_2 = data2.loc[data2_month == month]
    data2_money = data2_2['实际金额'].sum()
    return data2_money
def task2_2_2(position1,position2):
    position2 = []
    for i in range(12):
        temp = task2_2(r'' + position1,i + 1)
        position2.append(temp)
    return position2
A = task2_2_2("task1-1A.csv",'A')  
B = task2_2_2('task1-1B.csv','B')
C = task2_2_2('task1-1C.csv','C')
D = task2_2_2('task1-1D.csv','D')
E = task2_2_2('task1-1E.csv','E')
x=[1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x,A)
plt.plot(x,B)
plt.plot(x,C)
plt.plot(x,D)
plt.plot(x,E)
plt.legend(['A','B','C','D','E'])
plt.xticks(range(13))
plt.xlabel('月份')
plt.ylabel('月总交易额')
plt.show()


# In[19]:


A


# In[26]:


def task2_2_3(position,position_month):
    position_month = []
    for i in range(1,12):
        temp = round((position[i] - position[i - 1])/position[i - 1],2)
        position_month.append(temp)
    return position_month
A_month = task2_2_3(A,'A_month')
B_month = task2_2_3(B,'B_month')
C_month = task2_2_3(C,'C_month')
D_month = task2_2_3(D,'D_month')
E_month = task2_2_3(E,'E_month')
p1 = plt.figure(figsize=(15,8))## 设置画布
plt.rcParams['font.sans-serif'] = 'SimHei'## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('月份')
plt.ylabel('月环比增长率')
month2 = np.arange(2,13)
plt.bar(month2 - 0.3,A_month,width=0.15,label='A')
plt.bar(month2 - 0.15,B_month,width=0.15,label='B')
plt.bar(month2,C_month,width=0.15,label='C')
plt.bar(month2 + 0.15,D_month,width=0.15,label='D')
plt.bar(month2 + 0.3,E_month,width=0.15,label='E')
plt.title("交易额月环比增长率")
plt.legend()
plt.show()


# In[27]:


def profit(position):
    data1 = pd.read_csv(r'' + position,encoding = 'gbk')
    data2 = pd.read_csv(r'C:\Users\34367\Desktop\新零售-前置知识数据及代码\项目数据\附件2.csv',encoding = 'gbk')
    temp = pd.merge(data1,data2)
    drinks = temp.loc[temp['大类'] == '饮料']
    noDrinks = temp.loc[temp['大类'] == '非饮料']
    income = drinks['实际金额'].sum() * 0.25 + noDrinks['实际金额'].sum() * 0.2
    income = round(income,2)
    return income
profitA = profit('task1-1A.csv')
profitB = profit('task1-1B.csv')
profitC = profit('task1-1C.csv')
profitD = profit('task1-1D.csv')
profitE = profit('task1-1E.csv')
import matplotlib.pyplot as plt
profit = [profitA,profitB,profitC,profitD,profitE]
labels = ['A','B','C','D','E']
plt.pie(profit,labels = labels ,autopct="%1.2f%%")
plt.show()


# In[28]:


data1 = pd.read_csv(r'C:\Users\34367\Desktop\新零售-前置知识数据及代码\项目数据\附件1.csv' ,encoding = 'gbk')
data1 = data1.drop([70679])
data2 = pd.read_csv(r'C:\Users\34367\Desktop\新零售-前置知识数据及代码\项目数据\附件2.csv',encoding = 'gbk')
mergeData = pd.merge(data1,data2)
mergeData['支付时间'] = pd.to_datetime(mergeData['支付时间'])  
mergeData_month = pd.to_datetime(mergeData['支付时间']).dt.month
def task2_4(month,secondClass):
    temp = mergeData.loc[mergeData_month == month]
    productMean = temp[temp['二级类'] == secondClass]['实际金额'].mean()
    productMean = round(productMean,2)
    return productMean
A0 = []
for i in range(12):
    meanProduct = task2_4(i + 1,'乳制品')
    A0.append(meanProduct)
A1 = []
for i in range(12):
    meanProduct1 = task2_4(i + 1,'其他')
    A1.append(meanProduct1)
    
A2 = []
for i in range(12):
    meanProduct2 = task2_4(i + 1,'功能饮料')
    A2.append(meanProduct2)   
A3 = []
for i in range(12):
    meanProduct3 = task2_4(i + 1,'咖啡')
    A3.append(meanProduct3)   
A4 = []
for i in range(12):
    meanProduct4 = task2_4(i + 1,'坚果炒货')
    A4.append(meanProduct4)    
A5 = []
for i in range(12):
    meanProduct5 = task2_4(i + 1,'方便速食')
    A5.append(meanProduct5)    
A6 = []
for i in range(12):
    meanProduct6 = task2_4(i + 1,'果冻/龟苓膏')
    A6.append(meanProduct6)
A7 = []
for i in range(12):
    meanProduct7 = task2_4(i + 1,'果蔬饮料')
    A7.append(meanProduct7)    
A8 = []
for i in range(12):
    meanProduct8 = task2_4(i + 1,'植物蛋白')
    A8.append(meanProduct8)   
A9 = []
for i in range(12):
    meanProduct9 = task2_4(i + 1,'水')
    A9.append(meanProduct9)
A10 = []
for i in range(12):
    meanProduct10 = task2_4(i + 1,'海味零食')
    A10.append(meanProduct10)    
A11 = []
for i in range(12):
    meanProduct11 = task2_4(i + 1,'碳酸饮料')
    A11.append(meanProduct11)
A12 = []
for i in range(12):
    meanProduct12 = task2_4(i + 1,'糖果/巧克力')
    A12.append(meanProduct12)
A13 = []
for i in range(12):
    meanProduct13 = task2_4(i + 1,'纸巾')
    A13.append(meanProduct13)
A14 = []
for i in range(12):
    meanProduct14 = task2_4(i + 1,'肉干/豆制品/蛋')
    A14.append(meanProduct14)
A15 = []
for i in range(12):
    meanProduct15 = task2_4(i + 1,'膨化食品')
    A15.append(meanProduct15)
A16 = []
for i in range(12):
    meanProduct16 = task2_4(i + 1,'茶饮料')
    A16.append(meanProduct16)
A17 = []
for i in range(12):
    meanProduct17 = task2_4(i + 1,'蜜饯/果干')
    A17.append(meanProduct17)
A18 = []
for i in range(12):
    meanProduct18 = task2_4(i + 1,'饼干糕点')
    A18.append(meanProduct18)
A19 = []
for i in range(12):
    meanProduct19 = task2_4(i + 1,'香烟')
    A19.append(meanProduct19)  
plt.rcParams['font.sans-serif'] = 'SimHei'## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(15,15))
x = [1,2,3,4,5,6,7,8,9,10,11,12]
color = np.random.rand(len(A0))
plt.scatter(x,A0,s = np.array(A0) * 50)
plt.scatter(x,A1,s = np.array(A1) * 50)
plt.scatter(x,A2,s = np.array(A2) * 50)
plt.scatter(x,A3,s = np.array(A3) * 50)
plt.scatter(x,A4,s = np.array(A4) * 50)
plt.scatter(x,A5,s = np.array(A5) * 50)
plt.scatter(x,A6,s = np.array(A6) * 50)
plt.scatter(x,A7,s = np.array(A7) * 50)
plt.scatter(x,A8,s = np.array(A8) * 50)
plt.scatter(x,A9,s = np.array(A9) * 50)
plt.scatter(x,A10,s = np.array(A10) * 50)
plt.scatter(x,A11,s = np.array(A11) * 50)
plt.scatter(x,A12,s = np.array(A12) * 50)
plt.scatter(x,A13,s = np.array(A13) * 50)
plt.scatter(x,A14,s = np.array(A14) * 50)
plt.scatter(x,A15,s = np.array(A15) * 50)
plt.scatter(x,A16,s = np.array(A16) * 50)
plt.scatter(x,A17,s = np.array(A17) * 50)
plt.scatter(x,A18,s = np.array(A18) * 50)
plt.scatter(x,A19,s = np.array(A19) * 50)
plt.legend(['乳制品','其他','功能饮料','咖啡','坚果炒货','方便速食','果冻/龟苓膏','果蔬饮料','植物蛋白','水','海味零食','碳酸饮料','糖果/巧克力','纸巾','肉干/豆制品/蛋','膨化食品','茶饮料','蜜饯/果干','饼干糕点','香烟'])
plt.show()


# In[30]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 读取文件
data1 = pd.read_csv(r'C:\Users\34367\Desktop\新零售-前置知识数据及代码\项目数据\附件1.csv',encoding = 'gbk')
#去除异常数据
data1 = data1.drop([70679])
data2 = pd.read_csv(r'C:\Users\34367\Desktop\新零售-前置知识数据及代码\项目数据\附件2.csv',encoding = 'gbk')
#合并文件
merge_data = pd.merge(data1,data2)
merge_data['支付时间'] = pd.to_datetime(merge_data['支付时间'])
merge_data['月份'] = merge_data['支付时间'].dt.month
merge_data1 = merge_data.loc[merge_data['大类'] == '饮料']
retail_A = merge_data1.loc[merge_data1['地点'] == 'A']
retail_B = merge_data1.loc[merge_data1['地点'] == 'B']
retail_C = merge_data1.loc[merge_data1['地点'] == 'C']
retail_D = merge_data1.loc[merge_data1['地点'] == 'D']
retail_E = merge_data1.loc[merge_data1['地点'] == 'E']
def NoteTags(data,down, up, filename):
    #按商品进行分组并计数
    grouped = data.groupby('商品').count()
    
    grouped['销量占比'] = grouped['订单号'] / len(grouped)
    
    #按‘销量占比’的值排序
    grouped = grouped.sort_values(by = '销量占比')
    
    #计算分位数
    per_20 = grouped.loc[:, '销量占比'].quantile(down)
    per_80 = grouped.loc[:, '销量占比'].quantile(up)
    
    #根据销量占比与分位数的比较，定义销量标签
    for i in grouped.index:
        #print(i)
        if (grouped.loc[i, '销量占比'] < per_20):
            grouped.loc[i, '销量标签'] = '滞销'
        elif (grouped.loc[i, '销量占比'] > per_80):
            grouped.loc[i, '销量标签'] = '热销'
        else:
            grouped.loc[i, '销量标签'] = '正常'
    
    #删除不必要的列
    grouped.drop(['订单号','设备ID','应付金额','实际金额','支付时间','地点','状态','提现','大类','二级类','销量占比'],
                 axis=1,inplace=True)
    
    grouped.to_csv(filename, index = True, encoding = 'gbk')
    return grouped
grouped_a = NoteTags(retail_A, 0.20, 0.80, 'task3-1A.csv')
grouped_b = NoteTags(retail_B, 0.20, 0.80, 'task3-1B.csv')
grouped_c = NoteTags(retail_C, 0.20, 0.80, 'task3-1C.csv')
grouped_d = NoteTags(retail_D, 0.20, 0.80, 'task3-1D.csv')
grouped_e = NoteTags(retail_E, 0.20, 0.80, 'task3-1E.csv')
def num_set(data):
    for i in data.index:
        #print(i)
        if (data.loc[i, '销量标签'] == '滞销' ):
            data.loc[i, 'num'] = 10
        elif (data.loc[i, '销量标签'] == '正常'):
            data.loc[i, 'num'] = 40
        else:
            data.loc[i, 'num'] = 70
num_set(grouped_a)
num_set(grouped_b)
num_set(grouped_c)
num_set(grouped_d)
num_set(grouped_e)
get_ipython().system('pip install wordcloud')
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def DrawWordCloud(data,font):
            
    ss = pd.Series(data.loc[:, 'num'], index = data.index)
    

    wc = WordCloud( font_path = font,#设置字体  
                    background_color = "white", #背景颜色     
                    max_font_size = 100,  #字体最大值  
                    min_font_size = 10, #显示的最小的字体大小
                    random_state = 42
                    )
    
    gar_wordcloud = wc.fit_words(ss)  # num是由频数构成的Series的形式，且商品作为索引
    plt.figure(figsize=(16,8))
    plt.imshow(gar_wordcloud)
    plt.axis('off') 
    plt.show() 
DrawWordCloud(grouped_a,'C:\\Windows\\Fonts\\simhei.ttf')
DrawWordCloud(grouped_b,'C:\\Windows\\Fonts\\simhei.ttf')
DrawWordCloud(grouped_c,'C:\\Windows\\Fonts\\simhei.ttf')
DrawWordCloud(grouped_d,'C:\\Windows\\Fonts\\simhei.ttf')
DrawWordCloud(grouped_e,'C:\\Windows\\Fonts\\simhei.ttf')


# In[ ]:




