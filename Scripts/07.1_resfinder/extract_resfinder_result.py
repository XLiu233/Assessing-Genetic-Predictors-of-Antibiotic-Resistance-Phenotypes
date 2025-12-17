import os
import pandas as pd

BASE_DIR = "output"

from pathlib import Path

folder_path = Path(BASE_DIR) 

ResFinder_df = pd.DataFrame(columns=["Resistance_gene", "Best_Identities", "Alignment Length/Gene Length", "Coverage", "Position_in_reference", "Contig", "Position in contig", "Antibiotic", "Accession no.", "Percentage Length of Reference Sequence", "isolateID"])
for folder_name in os.listdir(BASE_DIR):
    isolateID = folder_name.split(".")[0]
    if os.path.exists(f"{BASE_DIR}/{folder_name}/ResFinder_results_table.txt"):
        folder_content = open(f"{BASE_DIR}/{folder_name}/ResFinder_results_table.txt", "r")
    else:
        continue
    file_lines = folder_content.readlines()
    for line in file_lines:
        if "	" in line and "Resistance" not in line:
            new_row_data = line.replace("\n","").split("	")
            percentage_length = int(new_row_data[2].split("/")[0])/int(new_row_data[2].split("/")[1])
            percentage_length *=100
            formatted_number = f"{percentage_length:.3f}"
            new_row_data.append(formatted_number)
            new_row_data.append(isolateID.rsplit('_', 1)[0])
            # Convert Antibiotic column to lower case
            new_row_data[7] = new_row_data[7].lower()
            # Convert the list to a Series with appropriate index (column names)
            new_row_series = pd.Series(new_row_data, index=ResFinder_df.columns)
            # Append the Series as a new row using concat
            ResFinder_df = pd.concat([ResFinder_df, new_row_series.to_frame().T], ignore_index=True)

ResFinder_df.to_csv("ResFinder_results.csv")


