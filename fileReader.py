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
import math


# def convertTuple(tup):
#     str = ''.join(tup)
#     return str

# startTime = datetime.now()
class FileReader:
    sheets = []
    row_quantity = 0

    def __init__(self, filenameExcel):
        self.wb = openpyxl.load_workbook(filenameExcel, read_only=True)
        for x in self.wb.sheetnames:
            if x.find("Vertical") == 0:
                self.sheets.append(x)
        for x in self.sheets:
            self.row_quantity += self.wb[x].max_row
        # print(self.row_quantity)

        b = 0

        z = []

        # print("Sheets to be processed -> " + str(len(self.sheets)))

        for sheet in self.sheets:
            data = self.wb[sheet].rows

            toolbar_width = math.ceil(self.wb[sheet].max_row / 40000)
            # print(toolbar_width)

            b = 0

            # print(sheet + " rows quantity:\n" +  + " items")

            sys.stdout.write("[%s] rows to be processed =>%s" % (" " * (int(toolbar_width)), str(self.wb[sheet].max_row)))
            sys.stdout.flush()
            sys.stdout.write("\b" * (31 + int(toolbar_width)))  # return to start of line, after '['

            for row in data:
                l = list(row)
                x = ""

                for i in range(len(l)):
                    if i == len(l) - 1:
                        x += str(l[i].value)
                    else:
                        x += (str(l[i].value) + ',')
                z.append(x)

                if b % 40000 == 0:
                    sys.stdout.write("#")
                    sys.stdout.flush()
                b = b + 1
            sys.stdout.write("]\n")  # this ends the progress bar
        self.wb.close()