import pandas as pd
import time

print(time.time())
fileConcordia = pd.read_excel(r"C:\Users\lkouteich\Desktop\student_data\Concordia.xlsx")
fileMcGill = pd.read_excel(r"C:\Users\lkouteich\Desktop\student_data\McGill.xlsx")
fileTrebas = pd.read_excel(r"C:\Users\lkouteich\Desktop\student_data\TREBAS.xlsx")
fileConcordia.rename(columns={'Student_Code':'Student_ID', 'Nationality':'Country'}, inplace=True)
fileMcGill.rename(columns={'id':'Student_ID','name':'Full_Name','city':'City', 'country':'Country', 'Course':'Program'}, inplace=True)
fileTrebas['Full_Name'] = fileTrebas.First_Name.str.cat(fileTrebas.Last_Name, sep=' ')
fileTrebas.drop(labels=['First_Name', 'Last_Name', 'City'], axis=1, inplace=True)
fileMcGill.drop(labels=['City'], axis=1, inplace=True)
fileConcordia['Student_ID'] = fileConcordia['Student_ID'].astype(str)
fileMcGill['Student_ID'] = fileMcGill['Student_ID'].astype(str)
fileTrebas['Student_ID'] = fileTrebas['Student_ID'].astype(str)

frames = [fileTrebas, fileMcGill, fileConcordia]
fileResult = pd.concat(frames)

fileResult.to_excel(r'C:\Users\lkouteich\Desktop\student_data\filename.xlsx')
print(time.time())

