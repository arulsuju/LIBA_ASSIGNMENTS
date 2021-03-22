import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
#Reading the data from Excel
pdf=pd.read_excel('Table 15.1 InternetUsage.xlsx')
#Printing the data
H0="Internet Usage of Male and Female are same"
H1="Internet Usage of Male and Female are NOT same"
print (pdf)
s=pdf
sm=s[s['GENDER']==2] #male
sf=s[s['GENDER']==1] #female
t1=stats.ttest_ind(sm.IUSAGE,sf.IUSAGE,equal_var = True)
print (t1)
if(t1.pvalue < 0.05):
    print("Reject H0 :"+H1)
else:
    print("Accept HO :"+H0)
t2=stats.ttest_ind(sm.IUSAGE,sf.IUSAGE,equal_var = False)
print(t2)

"""
Ttest_indResult(statistic=-4.491645814845378, pvalue=0.00011115562847277297)
Reject H0 :Internet Usage of Male and Female are NOT same
"""


