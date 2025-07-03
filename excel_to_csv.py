import os 
import pandas as pd 

folder_path = r"F:\automation_dummy file"

for x in os.listdir(folder_path):
    if x.endswith(".xlsx"):
     excel_path = os.path.join (folder_path,x)
    df = pd.read_excel(excel_path)
    csv = x.replace(".xlsx",".csv")
    csv_path = os.path.join(folder_path,csv)
    df.to_csv(csv_path,index=False)

print ("excel to csv complet successfully")
 
