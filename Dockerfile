FROM python:3.10.5
ADD Attendance.py .
RUN pip install pandas
RUN pip install numpy
RUN pip install openpyxl
RUN pip install requests
RUN pip install timer
RUN pip install datetime

COPY Attendance.xlsx /

EXPOSE 3333
CMD ["python","./Attendance.py"]