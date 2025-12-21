#might have to do this eventually
#Right now, put functions.py where you execute this
#
import sys

#make sure this points to functions folder
#This will work assuming you are working in analysis
sys.path.append('../Scripts/functions/')

#import all functions
from functions_10_interval_checkM import *

import pandas as pd
import math
import random

#not sure what this small test is
#xls = pd.ExcelFile("small data set test.xlsx")
#changed to import excel files directly
df1 = pd.read_csv('CARD_results.csv')
df1 = df1.fillna('')
#remove sheet 2 from Gray et al SI table 2
df2 = pd.read_csv('es0c03803_si_002.csv')

df3 = pd.read_csv('checkm2_results.csv')
checkM_dict = mkCheckM(df3)
checkM_allow_list = filterCheckM(checkM_dict)

# print(checkM_block_list)




#old phenotype data by class
#df2 = pd.read_excel('phenotype data.xls')

phenotype_dict = {}
rows = []
rows=mkrows(df2)
random.shuffle(rows)

phenotype_dict=mkphenofromrow(rows)
print("before remove phenotype_dict have {} keys".format(len(phenotype_dict)))
for key in list(phenotype_dict):
   if key not in checkM_allow_list:
       phenotype_dict.pop(key)
print("after remove allowed phenotype_dict have {} keys".format(len(phenotype_dict)))


#Is this used?
#resistance_dict = {}

CARD_dict = {}
rows = []
CARD_dict=mkCARDdict(df1)
print("before remove CARD_dict have {} keys".format(len(CARD_dict)))
for key in list(CARD_dict):
    if key not in checkM_allow_list:
        CARD_dict.pop(key)
print("after remove allowed CARD_dict have {} keys".format(len(CARD_dict)))

CARD_dict = {}
rows = []
CARD_dict=mkCARDdict(df1)

#Is this used? If so, where?
import seaborn as sn

df=mkconfusion(CARD_dict,phenotype_dict,pd)
