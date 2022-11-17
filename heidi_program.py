import pandas as pd
from pandas import DataFrame
import glob
import matplotlib.pyplot as plt
import numpy as np
import statistics
from camelcase import CamelCase

path = "C:/downloads"
cs = CamelCase()

df = pd.read_excel(r'C:\Users\Heidi\Downloads\average.xlsx')


def print_names():
    names = df["Student_Name"]
    temp_name = []
    for i in names:
        # print(cs.hump(i))
        temp_name.append(cs.hump(i))
    return temp_name


def average_grades():
    grades = df["Average"].mean()
    return grades
    # print(grades)


# Label Grades
def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')


# x = list(df.iloc[:, 0])
y_axis = list(df.iloc[:, 1])

# size
f = plt.figure()
f.set_figwidth(5)
f.set_figheight(5)

# Plot the data using bar() method
plt.bar(print_names(), y_axis, color='g')
plt.title("Students Grades")
plt.xlabel("Names")
plt.ylabel("Grades")

# Axis Labels

plt.xticks(rotation=45, ha='right', fontsize=5)

addlabels(print_names(), y_axis)

# Average calculation
plt.text(4, 95, 'Average Grade: ' + str(average_grades()), fontsize=7,
         bbox=dict(facecolor='red', alpha=0.5))

# Show the plot
plt.savefig("heidi_graph.png")