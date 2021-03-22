import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
#Reading the data from Excel
pdf=pd.read_excel('Table 15.1 Nike.xlsx')
#Printing the data
H0="Attitude of Male and Female are same"
H1="Attitude of Male and Female are NOT same"
print (pdf)
s=pdf.drop(['caseno'],axis=1)
sm=s[s['gender']==2] #male
sf=s[s['gender']==1] #female
print("********** T Test for independent Variables - EQUAL Variance assumed to be true **********")
t1=stats.ttest_ind(sm.attitude,sf.attitude,equal_var = True)
print (t1)
if(t1.pvalue < 0.05):
    print("Reject H0 :"+H1)
else:
    print("Accept HO :"+H0)
"""
Ttest_indResult(statistic=2.1935541062097075, pvalue=0.033721905507208036)
Reject H0 :Attitude of Male and Female are NOT same
"""
#T test for the independent samples where Equal Variances NOT Assumed
print("********** T Test for independent Variables - EQUAL Variance Not assumed**********")
t2=stats.ttest_ind(sm.awarenes,sf.awarenes,equal_var = False)
print(t2)
if(t1.pvalue < 0.05):
    print("Reject H0 :"+H1)
else:
    print("Accept HO :"+H0)
"""
Ttest_indResult(statistic=1.8675080099100607, pvalue=0.06877620594794934)
Reject H0 :Attitude of Male and Female are NOT same
"""
#One Sample T test for checking the awarenes
print("********** ONE Sample t test for checking Mean **********")
t3=stats.ttest_1samp(pdf.awarenes,5.0)
print(t3)

#Test for Onway Anova
print("********** ONE Way Anova **********")
t4=stats.f_oneway(sm.attitude,sf.attitude)
print(t4)
