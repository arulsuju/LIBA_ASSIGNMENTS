import pandas as pd
from scipy import stats
pdf=pd.read_excel('Table 15.1 Nike.xlsx')
print (pdf)
s=pdf.drop(['caseno'],axis=1)
sm=s[s['gender']==2] #male
sf=s[s['gender']==1] #female
t1=stats.ttest_ind(sm.attitude,sf.attitude,equal_var = True)
print (t1.pvalue)