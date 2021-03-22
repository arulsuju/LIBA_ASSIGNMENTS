import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
#Reading the data from Excel
pdf=pd.read_excel('ChickenWeight.xlsx')
#Printing the data
H0="Diet of Group1 and Group2 are same"
H1="Diet of Group1 and Group2 are NOT same"
print (pdf)
s=pdf
sm=s[s['Diet']==1] #Diet1
sf=s[s['Diet']==2] #Diet2
t1=stats.ttest_ind(sm.weight,sf.weight,equal_var = True)
print (t1)
if(t1.pvalue < 0.05):
    print("Reject H0 :"+H1)
else:
    print("Accept HO :"+H0)
"""
Ttest_indResult(statistic=-2.8233497803117458, pvalue=0.0050341326141437855)
Reject H0 :Diet of Group1 and Group2 are NOT same
"""

