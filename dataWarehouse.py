import os
import pandas as pd
import openpyxl
import xlwt
import fsspec

base_path = 'C:\\Users\\lkouteich\\Desktop\\student_data\\'

file_count = 0
files_namelist = []
data_setList = []
outputFile = 'output.xlsx'

for file in os.listdir(base_path):
    if os.path.isfile(os.path.join(base_path, file)):
        file_count += 1
        files_namelist.append(file)


for file_name in files_namelist:
    dataset = pd.read_excel(base_path+file_name)
    data_setList.append(dataset)

with pd.ExcelWriter(base_path+outputFile) as writer:
    for i in range(len(data_setList)):
        data_setList[i] = data_setList[i].assign(college=files_namelist[i].split('.')[0])
        data_setList[i].to_excel(writer, sheet_name=files_namelist[i].split('.')[0], index=False)

print('Assignment done')