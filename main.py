#!/usr/bin/python

import sys
from collections import deque

from configsReader import ConfigsReader
from fileReader import FileReader
from Analyzer import Analyzer, Switcher

def menu():
    print("Please,select an option: \n1. Print list of FIDs with problems;\n2. Stop execution of the program\n")

def main(filename):
    if len(sys.argv) == 1:
        print("Usage details: please add filename.")
        sys.exit
    elif len(sys.argv) > 2:
        print("Usage details: only on file can be selected.")
        sys.exit
    else:
        AcceptableGeneralMismatchListVar = deque(ConfigsReader().getAcceptableGeneralMismatchList())
        AcceptableGeneralSpecializedListVar = deque(ConfigsReader().getAcceptableSpecialysedMismatchList())

        print(AcceptableGeneralSpecializedListVar)
        Data_to_analyze = FileReader(filename).getDataForAnalysis()

        SwitcherVar = Switcher(Data_to_analyze, AcceptableGeneralMismatchListVar)

        while 1:
            menu()
            option = input()
            SwitcherVar.execute_option(option)
            continue


if __name__ == "__main__":
    main(sys.argv[1])
# _, a, b = sys.argv
# for filename
# except Exeptioin as e:
# 	print(type(e))

# # Opening a file
# file1 = open('test', 'w')
#
# # Writing a string to file
# for x in z:
#     file1.write(x + '\n')
#
# # Writing multiple strings
# # at a time
# # file1.writelines(L)
#
# # Closing file
# file1.close()
# # print(z)