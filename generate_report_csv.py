#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []
    for employee in employee_file:
        employee_list.append(employee)

    return employee_list

def process_data(employee_list):
    department_list = []
    for employee in employee_list:
        department_list.append(employee["Department"])

    #print("\n",department_list)
    department_data ={}
    for department_name in set(department_list):
        department_data[department_name]= department_list.count(department_name)

    return department_data

def write_report(dictionary, report_file):
    with open(report_file, "w+") as file:
        for k in sorted(dictionary):
            file.write(str(k) + ":" + str(dictionary[k]) + "\n")
        file.close()


employee_list = read_employees("employee.csv")
print(employee_list)

dictionary = process_data(employee_list)
#print("/n")
print(dictionary)

write_report(dictionary,"report.txt")

