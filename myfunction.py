import numpy as np
from camelcase import CamelCase
import math
import statistics as st
import matplotlib.pyplot as mp

class Student:

    student_data = {"students":[{"first_name":"Vijay","last_name":"singh","mark":20},
                                {"first_name":"carl","last_name":"deek","mark":50},
                                {"first_name":"Valentina","last_name": "arenas","mark":70},
                                {"first_name":"adithya","last_name":"ramshankar","mark":100}]}

    cs = CamelCase()
    student_name: []


    def return_student_name(self):
        temp_student_name = []
        for item in self.student_data['students']:
            temp_student_name.append(self.cs.hump(item.get('first_name') + ' ' + item.get('last_name')))
        return temp_student_name

    def return_student_marks(self):
        temp_student_marks = []
        for item in self.student_data['students']:
            temp_student_marks.append(item['mark'])
        return temp_student_marks

    def return_graph(self):
        graph_figure = mp.figure()
        graph_figure.set_figwidth(5)
        graph_figure.set_figheight(10)
        return graph_figure

    def addlabels(self,x, y):
        for i in range(len(x)):
            mp.text(i, y[i], y[i], ha='center')

    def return_bar_graph(self):
        self.return_graph()
        mp.bar(self.return_student_name(),self.return_student_marks(), color='g')
        mp.title("Student Grades")
        mp.xlabel("Names")
        mp.ylabel("Grades")
        mp.xticks(rotation=45, ha='right', fontsize=5)
        self.addlabels(self.return_student_name(),self.return_student_marks())
        self.return_average(self.return_student_marks())
        mp.savefig("mygraph.png")

    def return_average(self,x):
        mp.text(.5,95,'Average Grade of class is: '+str(st.mean(x)), fontsize=7,
                 bbox=dict(facecolor='red', alpha=0.5))



user = Student()
user.return_student_name()
user.return_bar_graph()