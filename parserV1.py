import csv
from tabulate import tabulate
from pandas import pandas
# import datetime from datetime
# firstpath = D://
# secondpath = D://
def load_data(filename):
    mylist =[]
    with open(filename) as numbers:
        numbers_data = csv.reader(numbers, delimiter=',')
        next(numbers_data) #skip the header
        for row in numbers_data:
            mylist.append(row)
        return mylist

min = 1.0
max = 1.8

new_list = load_data('data.csv')
ng_list = []
for row in new_list:
    if row[2] == "false":
        for col in range(3,6):
            if (float(row[col]) < min or float(row[col]) > 1.8): 
                ng_list[row].append(row[col])
                # ng_list[1].append(row[1])
                # print(row[col],'',row[1])
                # print(row[1])
                # print("\n")
print(tabulate(ng_list))