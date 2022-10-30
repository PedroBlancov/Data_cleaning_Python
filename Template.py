import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline

data=pd.read_excel('')

data=data.drop(data[[]],axis=1)
data.head()

cust_count=data.groupby('').count()['']
label=data.groupby('').count()[''].index


plt.axis('')
plt.pie(cust_count, labels=label, shadow=True, autopct='%1.2f%%', radius=2, explode=[0.3,0.3,0.2,0.1,0.1])
plt.show

wine_spent=data.groupby('').mean()['']

meat_spent=data.groupby('').mean()['']
fish_spent=data.groupby('').mean()['']
sweet_spent=data.groupby('').mean()['']
gold_spent=data.groupby('').mean()['']

plt.figure(figsize=(17,10))
plt.bar(xpos-0.45,wine_spent,width=0.15,label='',color='pink')
plt.bar(xpos-0.3,fruit_spent,width=0.15,label='',color='purple')
plt.bar(xpos-0.15,meat_spent,width=0.15,label=' ',color='red')
plt.bar(xpos,fish_spent,width=0.15,label=' ',color='blue')
plt.bar(xpos+0.15,sweet_spent,width=0.15,label='',color='brown')
plt.bar(xpos+0.3,gold_spent,width=0.15,label=' ',color='yellow')

plt.xticks(xpos,label)
plt.ylabel('   ')
plt.title('  ')
plt.legend(loc='best',shadow=True,fontsize='large')
