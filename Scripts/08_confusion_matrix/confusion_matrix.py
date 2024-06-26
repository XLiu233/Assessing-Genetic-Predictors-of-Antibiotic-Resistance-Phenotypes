
import pandas as pd
import math
import random

xls = pd.ExcelFile("small data set test.xlsx")
df1 = pd.read_excel(xls, 'CARD Full results')
df2 = pd.read_excel(xls, 'phenotype data')
phenotype_dict = {}
rows = []
for index,row in df2.iterrows():
  if index <=2:
    continue
  rows.append((index,row))
random.shuffle(rows)
for index, row in rows:
  isolateId = row['isolateID']
  phenotype_dict[isolateId] = []
  phenotype_dict[isolateId].append(row['penam'])
  phenotype_dict[isolateId].append(row['macrolide1'])
  phenotype_dict[isolateId].append(row['macrolide2'])
  phenotype_dict[isolateId].append(row['tetracycline'])
  phenotype_dict[isolateId].append(row['aminoglycoside'])
  phenotype_dict[isolateId].append(row['fluoroquinolone'])
  phenotype_dict[isolateId].append(row['sulfonamide'])
  phenotype_dict[isolateId].append(row['peptide'])
  phenotype_dict[isolateId].append(row['phenicol'])
resistance_dict = {}


CARD_dict = {}
rows = []
for index,row in df1.iterrows():
  rows.append((index,row))
random.shuffle(rows)
for index, row in rows:
  isolateId = row['isolateID'].rsplit('_', 1)[0]
  if isolateId not in CARD_dict:
    CARD_dict[isolateId] = []
  data = []
  data.append(row['Percentage Length of Reference Sequence'])
  data.append(row['Best_Identities'])
  data.append(row['Drug Class'])
  CARD_dict[isolateId].append(data)


import seaborn as sn

targets = ["penam","macrolide","macrolide","tetracycline","aminoglycoside","fluoroquinolone","sulfonamide","peptide","phenicol"]
df=[[-1 for i in range(101)] for j in range(121)]
for length in range(0,121,1):
  for identity in range(0,101,1):
    m1 = [0,0,0,0]
    for isolateId in CARD_dict:
      drugs = ""
      if isolateId not in phenotype_dict:
        continue
      for data in CARD_dict[isolateId]:
        if data[0] >= length  and data[1] >= identity:
          drugs = drugs + data[2]
      start_index = 0
      for target in targets:
        if pd.isna(drugs):
          continue
          # TP
        if target.lower() in drugs.lower() and (phenotype_dict[isolateId][start_index]==1 or phenotype_dict[isolateId][start_index]==0):
          m1[0]+=1
          # TN
        if not target.lower() in drugs.lower() and (phenotype_dict[isolateId][start_index]==-1):
          m1[1]+=1
          # FP
        if target.lower() in drugs.lower() and phenotype_dict[isolateId][start_index]==-1:
          m1[2]+=1
          # FN
        if not target.lower() in drugs.lower() and (phenotype_dict[isolateId][start_index]==1 or phenotype_dict[isolateId][start_index]==0):
          m1[3]+=1
        start_index+=1
    print(length,identity,m1[0],m1[1],m1[2],m1[3])
     # TP,TN,FP,FN
    df[length][identity] = m1
