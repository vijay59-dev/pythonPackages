import pandas
import openpyxl

concordia_file=pandas.read_excel("C:\MyDB\Excelfiles\Concordia.xlsx")
print(concordia_file)

mcgill_file=pandas.read_excel("C:\MyDB\Excelfiles\McGill.xlsx")
print(mcgill_file)

trebas_file=pandas.read_excel("C:\MyDB\Excelfiles\TREBAS.xlsx")
print(trebas_file)

anything=[trebas_file,concordia_file,mcgill_file]


with pandas.ExcelWriter('C:\MyDB\Excelfiles\hfile.xlsx') as writer:
    for i in range(len(anything)):
        anything[i].to_excel(writer, sheet_name=str(i))