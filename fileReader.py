#!/usr/bin/python

from datetime import datetime
import time
# from progress.bar import IncrementalBar
# from progress.bar import Bar
# from alive_progress import alive_bar
# from progress.bar import IncrementalBar

import csv
import sys
import xlrd
import pandas as pd
import openpyxl
from tqdm import tqdm


# def convertTuple(tup):
#     str = ''.join(tup)
#     return str

# startTime = datetime.now()
class FileReader:
    sheets = []
    row_quantity = 0

    def __init__(self, filenameExcel):
        # create a list with sheet numbers you want to process

        wb = openpyxl.load_workbook('4822_1.xlsx', read_only=True)
        for x in wb.sheetnames:
            if x.find("Vertical") == 0:
                self.sheets.append(x)
        for x in self.sheets:
            self.row_quantity += wb[x].max_row
        # print(self.row_quantity)

        b = 0

        z = []

        # bar = IncrementalBar('Countdown', max=100000)
        # # https://github.com/rsalmei/alive-progress
        for sheet in self.sheets:
            # print(sheet)
            data = wb[sheet].rows
            # print("sheet -" + sheet)

            b = wb[sheet].max_row

            for row in tqdm(data):
                l = list(row)
                x = ""
                # print(len(l))
                for i in range(len(l)):
                    if i == len(l) - 1:
                        x += str(l[i].value)
                    else:
                        x += (str(l[i].value) + ',')
                # print(x)
                # print(b)
                z.append(x)
                # if b == 100000:
                #     # print("woohoo")
                #     break
                b = b - 1

            # print(b)
            #     bar.next()
            # bar.finish()

            # # print(x.split(','))
            # # b = b + 1
            # # csv.write('\n')
            # # pbar.next()
        # # pbar.finish()

# print(datetime.now() - startTime)


# filename = '4822.xls'

## opening the xlsx file

# print(sheet.max_row)

# maxval = sheet.max_row
# # maxval = 100000
# import sys
#
# # pbar = Bar('Countdown', suffix='%(percent).1f%%', max = maxval)
# # pbar.start()
#
#
# # print('loaded')
# ## getting the data from the sheet
# data = sheet.rows
# # print(data)
# # print('loaded')
# ## creating a csv file
# # csv = open("data.csv", "w+")
# b = 0
#
# z = []
#
# # startTime = datetime.now()
#
# # # https://github.com/rsalmei/alive-progress
# with alive_bar(maxval, bar='classic', spinner='pulse') as bar:
#     for row in data:
#         l = list(row)
#         print(str(l))
#         x = ""
#         # print(len(l))
#         for i in range(len(l)):
#             if i == len(l) - 1:
#                 x += str(l[i].value)
#             else:
#                 x += (str(l[i].value) + ',')
#
#         z.append(x)
#         bar()
#         # if b == 100000:
#         # break
#         # b = b + 1
#     # # print(x.split(','))
#     # # b = b + 1
#     # # csv.write('\n')
#     # # pbar.next()
# # # pbar.finish()
# # with alive_bar(maxval, bar = 'classic', spinner = 'pulse') as bar:
# # for row in data:
# # l = list(row)
# # x= ""
# # # print(len(l))
# # for i in range(len(l)):
# # if i == len(l) - 1:
# # x += str(l[i].value)
# # else:
# # x += (str(l[i].value) + ',')
#
# # z.append(x)
# # bar()
#
# # with alive_bar(maxval, bar = 'classic', spinner = 'pulse') as bar:
# # for row in data:
# # l = list(row)
# # x= ""
# # # print(len(l))
# # for i in range(len(l)):
# # if i == len(l) - 1:
# # x += str(l[i].value)
# # else:
# # x += (str(l[i].value) + ',')
#
# # z.append(x)
# # bar()
#
# # with alive_bar(maxval, bar = 'classic', spinner = 'pulse') as bar:
# # for row in data:
# # l = list(row)
# # x= ""
# # # print(len(l))
# # for i in range(len(l)):
# # if i == len(l) - 1:
# # x += str(l[i].value)
# # else:
# # x += (str(l[i].value) + ',')
#
# # z.append(x)
# # bar()
#
# # with alive_bar(maxval, bar = 'classic', spinner = 'pulse') as bar:
# # for row in data:
# # l = list(row)
# # x= ""
# # # print(len(l))
# # for i in range(len(l)):
# # if i == len(l) - 1:
# # x += str(l[i].value)
# # else:
# # x += (str(l[i].value) + ',')
#
# # z.append(x)
# # bar()
#
# # with alive_bar(maxval, bar = 'classic', spinner = 'pulse') as bar:
# # for row in data:
# # l = list(row)
# # x= ""
# # # print(len(l))
# # for i in range(len(l)):
# # if i == len(l) - 1:
# # x += str(l[i].value)
# # else:
# # x += (str(l[i].value) + ',')
#
# # z.append(x)
# # bar()
# # print(datetime.now() - startTime)
#
# # startTime = datetime.now()
#
# for j in z:
#     # print(j)
#     if "!" in j:
#         q = j.split(',')
#         print(q)
#         if q[1] == 'ACT_FLAG3' and q[4] != '""' and q[5] != 'null':
#             print(q)
#
# # print(datetime.now() - startTime)
#
# # print(x)
# # print(z)
#
# ## close the csv file
# # csv.close()
#
#
# # with open('data.csv') as file:
# # line = csv.DictReader(file)
# # for row in line:
# # print(row['FID'] ,row ['FID'],row ['FID'])
#
#
# # print(datetime.now() - startTime)
