# This file is used to extract confusion matrix result into excel

import pandas as pd
df1 = pd.read_csv('CARD_results.csv')

checkM_block_list = ['tcs_031618_03', 'tcs_062317_10', 'bc_500_030218_07', 'tcs_051117_10_1', 'tcs_030218_03', 'tcs_051117_18', 'tcs_030218_10', 'bc_500_031618_03', 'tcs_101217_12', 'tcs_041417_10', 'tcs_052517_08', 'tcs_051117_15', 'tcs_020118_12', 'tcs_031017_01', 'tcs_101217_03', 'tcs_080317_02', 'tcs_121417_04', 'tcs_060917_11', 'tcs_031618_06', 'bc_250_030218_08', 'tcs_030218_05', 'bc_250_030218_06', 'tcs_102717_09', 'tcs_072017_07', 'tcs_041417_11', 'tcs_110917_09', 'tcs_101217_09', 'tcs_101217_05', 'tcs_031618_04', 'tcs_092117_06', 'tcs_031017_02', 'tcs_501', 'tcs_101217_07', 'tcs_031017_09', 'tcs_031017_07', 'tcs_082417_02', 'tcs_041417_05', 'tcs_060917_06', 'tcs_051117_07', 'tcs_051117_01', 'tcs_051117_05', 'tcs_052517_09', 'tcs_080317_04', 'tcs_052517_06', 'bc_500_040518_03', 'tcs_092117_10', 'tcs_110917_08', 'tcs_030218_06', 'bc_500_040518_02', 'tcs_101217_06', 'tcs_060917_10', 'tcs_110917_15', 'tcs_041417_04', 'bc_250_031618_06', 'tcs_060917_01', 'tcs_121417_08', 'tcs_052517_01', 'tcs_062317_08', 'tcs_060917_09', 'tcs_080317_08', 'tcs_051117_09', 'bc_250_020118_04', 'bc_500_040518_05', 'tcs_080317_03', 'tcs_052517_10', 'tcs_051017_08', 'tcs_080317_10', 'tcs_030218_04', 'tcs_062317_12', 'tcs_051017_13', 'tcs_102717_14', 'bc_250_031618_05', 'bc_250_040518_03', 'bc_250_040518_02', 'tcs_052517_02', 'tcs_051017_03', 'tcs_051017_09', 'tcs_031017_08', 'tcs_121417_09', 'tcs_031618_05', 'tcs_092117_04', 'tcs_092117_05', 'tcs_110917_12', 'tcs_092117_14', 'tcs_051117_14', 'tcs_110917_17', 'tcs_021617_05', 'tcs_030218_11', 'bc_500_020118_02', 'tcs_041417_01', 'tcs_121417_05', 'bc_250_012617_09', 'tcs_051117_19', 'tcs_021617_07', 'tcs_051017_18', 'tcs_110917_06', 'tcs_040518_04', 'tcs_020118_11', 'bc_500_031618_02', 'tcs_102717_01', 'tcs_052517_11', 'tcs_072017_04', 'tcs_101217_04', 'tcs_102717_15', 'tcs_092117_01', 'bc_500_030218_06', 'tcs_101217_08', 'tcs_051017_07', 'tcs_121417_06', 'tcs_040518_06', 'tcs_031618_02', 'tcs_051117_20', 'tcs_052517_04', 'bc_500_030218_01', 'tcs_092117_11', 'tcs_051017_02', 'tcs_051117_17', 'tcs_072017_05', 'bc_500_031618_04', 'tcs_102717_08', 'tcs_030218_08', 'tcs_051117_04', 'tcs_031017_12', 'tcs_110917_04', 'tcs_051117_16']
df2 = pd.read_csv('es0c03803_si_002.csv')

phenotype_dict = {}
rows = []
for index,row in df2.iterrows():
  if index ==0:
    continue
  rows.append((index,row))


for index, row in rows:
  isolateId = row['isolateID']
  phenotype_dict[isolateId] = []
  phenotype_dict[isolateId].append(row['tmp_res'])
  phenotype_dict[isolateId].append(row['amp_res'])
  phenotype_dict[isolateId].append(row['cip_res'])
  phenotype_dict[isolateId].append(row['tet_res'])
  phenotype_dict[isolateId].append(row['c_res'])
  phenotype_dict[isolateId].append(row['gm_res'])
  phenotype_dict[isolateId].append(row['azm_res'])
  phenotype_dict[isolateId].append(row['cl_res'])
  phenotype_dict[isolateId].append(row['er_res'])
resistance_dict = {}

print("before removal phenotype_dict have {} keys".format(len(phenotype_dict)))
for key in checkM_block_list:
    if key in phenotype_dict:
        phenotype_dict.pop(key)
print("after removal phenotype_dict have {} keys".format(len(phenotype_dict)))


CARD_dict = {}
rows = []
for index,row in df1.iterrows():
  rows.append((index,row))
for index, row in rows:
  isolateId = row['isolateID']
  if isolateId not in CARD_dict:
    CARD_dict[isolateId] = []
  data = []
  data.append(row['Percentage Length of Reference Sequence'])
  data.append(row['Best_Identities'])
  data.append(row['Antibiotic'])
  CARD_dict[isolateId].append(data)

print("before removal CARD_dict have {} keys".format(len(CARD_dict)))
for key in checkM_block_list:
    if key in CARD_dict:
        CARD_dict.pop(key)
print("after removal CARD_dict have {} keys".format(len(CARD_dict)))


targets = ["trimethoprim","ampicillin","ciprofloxacin","tetracycline","chloramphenicol","gentamicin","azithromycin","colistin","erythromycin"]

results = {}
c = 0
for isoId in CARD_dict:
  for row in CARD_dict[isoId]:
      if isoId not in phenotype_dict:
          continue
      key = isoId+str(row[0])+str(row[1])+str(row[2])
      drugs = row[2]
      start_index = 0
      results[key] = []

      for target in targets:

        if pd.isna(drugs):
          results[key].append("N/A")
          start_index+=1
          continue
        if pd.isna(phenotype_dict[isoId][start_index]):
          results[key].append("N/A")
          # TP
        if target.lower() in drugs.lower() and (phenotype_dict[isoId][start_index]==-1 or phenotype_dict[isoId][start_index]==0):
          results[key].append("TP")
          # TN
        if not target.lower() in drugs.lower() and (phenotype_dict[isoId][start_index]==1):
          results[key].append("TN")
          # FP
        if target.lower() in drugs.lower() and phenotype_dict[isoId][start_index]==1:
          results[key].append("FP")
          # FN
        if not target.lower() in drugs.lower() and (phenotype_dict[isoId][start_index]==-1 or phenotype_dict[isoId][start_index]==0):
          results[key].append("FN")

        start_index+=1


for  index,row in df1.iterrows():
  isolate_ID_short = row['isolateID']
  key = isolate_ID_short+str(row['Percentage Length of Reference Sequence'])+str(row['Best_Identities'])+str(row['Antibiotic'])
  if key not in results:
    continue

  df1.at[index, 'trimethoprim'] = results[key][0] if key in results else ""
  df1.at[index, 'ampicillin'] = results[key][1] if key in results else ""
  df1.at[index, 'ciprofloxacin'] = results[key][2] if key in results else ""
  df1.at[index, 'tetracycline'] = results[key][3] if key in results else ""
  df1.at[index, 'chloramphenicol'] = results[key][4] if key in results else ""
  df1.at[index, 'gentamicin'] = results[key][5] if key in results else ""
  df1.at[index, 'azithromycin'] = results[key][6] if key in results else ""
  df1.at[index, 'colistin'] = results[key][7] if key in results else ""
  df1.at[index, 'erythromycin'] = results[key][8] if key in results else ""


df1.to_excel("confusion_matrix_result_with_card.xlsx")
