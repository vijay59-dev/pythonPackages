import numpy
import pandas
import pandas as pd
import timer
from openpyxl import load_workbook
import datetime


class Attendance:

    todays_date = None
    student_names = numpy.array([])
    base_path = 'Attendance.xlsx'
    student_data_frame = None
    current_sheet = 'Middleware Tech'

# course list dictionary
    course_list: dict = {"course_list": [
   {"course_name": "Object Oriented Programming", "course_code": "420-PRB-TQ"},
   {"course_name": "Middleware Technology Extractors and Loaders", "course_code": "420-PRB-TQ"},
   {"course_name": "Predictive Modeling of Megadata", "course_code": "420-PMP-TQ"},
   {"course_name": "Non-transactional Master Data Analysis", "course_code": "420-ADM-TQ"},
   {"course_name": "Cybersecurity and Blockchain", "course_code": "420-CCB-TQ"},
   {"course_name": "Automation and Artificial Intelligence", "course_code": "420-ANA-TQ"},
   {"course_name": "Charts, Plans and Dashboards", "course_code": "420-DPT-TQ"},
   {"course_name": "Electronic Data Interchange", "course_code": "420-EDN-TQ"},
   {"course_name": "Predictive Analytics and Business Intelligence", "course_code": "420-APN-TQ"},
   {"course_name": "Computer Job Entry", "course_code": "420-NEN-TQ"},
   {"course_name": "Internship in Analytics, Megadata and Business Intelligence", "course_code": "420-AMN-TQ"}
]}

    def __init__(self):
        self.student_data_frame = pandas.read_excel(self.base_path,
                               sheet_name='Object Oriented Programming',skiprows=5)
        self.student_names = numpy.append(self.student_names,list(self.student_data_frame['Surname']))
        self.todays_date = datetime.datetime.now().strftime('%x')

    # method to prepare the template part 1
    def prepare_attendance_template_part1(self):
        temp_standard_template = pandas.read_excel(self.base_path,
                                                    sheet_name='Object Oriented Programming', nrows=3, usecols=lambda x: 'Unnamed' not in x)
        #to drop empty column
        temp_standard_template.dropna(axis=0, how='any', inplace=False)
        for i in range(len(self.course_list["course_list"])):
            if temp_standard_template.columns[1] == self.course_list.get('course_list')[i]['course_name']:
                temp_standard_template.columns.values[1] = self.course_list.get('course_list')[i+1]['course_name']
                temp_standard_template.values[0, 1] = self.course_list.get('course_list')[i+1]['course_code']
                break
            else:
                pass
        self.current_sheet = temp_standard_template.columns[1][0:15]
        return temp_standard_template, temp_standard_template.columns[1]

# method to prepare the template part 2
    def prepare_attendance_template_part2(self):
        temp_standard_template1 = pandas.read_excel(self.base_path,
                                                    sheet_name='Object Oriented Programming', skiprows=5, usecols=['Prog','Surname','Student TI#'])
        return temp_standard_template1

# consolidated method to prepare the template of new sheet and take attendance
    def prepare_template(self):
        first_part_of_template, sheet_name = self.prepare_attendance_template_part1()

        second_part_of_template = self.prepare_attendance_template_part2()

        with pd.ExcelWriter(self.base_path, mode='a', if_sheet_exists='overlay') as writer:
            first_part_of_template.to_excel(writer, sheet_name=sheet_name[0:15], index=False)
            second_part_of_template.to_excel(writer, sheet_name=sheet_name[0:15], index=False, startrow=6)

        self.take_attendance()

# function to take attendance
    def take_attendance(self):
        todays_attendance_list = []
        df = pd.read_excel(self.base_path,sheet_name=self.current_sheet, skiprows=6)

        #prompt user to take attendance
        for i in self.student_names:
            todays_attendance_list.append('P' if bool(input('Is '+i+' Present: ')) else 'A')
        todays_attendance_df = pd.DataFrame({self.todays_date: todays_attendance_list})

        with pd.ExcelWriter(self.base_path, mode='a', if_sheet_exists='overlay') as writer:
            todays_attendance_df.to_excel(writer, sheet_name=self.current_sheet, index=False, startrow=6, startcol=len(df.columns))

        timer.get_timer(5000)


#create class instance
teacher = Attendance()
while True:
    try:
        user_input = int(input('\n\nPlease enter the following number respective to the below given options\n'
                               '1. Create a new course sheet and take attendance\n'
                               "2. Take attendance of today's date\n"
                               '3. Quit Program\n\n\n'))

        if user_input <= 3:
            match int(user_input):
                case 1:
                    teacher.prepare_template()
                case 2:
                    teacher.take_attendance()
                case 3:
                    exit('Thank You for using attendance program')

        else:
            print('Please enter the given number to operate attendance sheet')
            continue
    except:
        print()
    finally:
        exit('Thank You for using attendance program')
