#!/usr/bin/python

import sys
from collections import deque

from configsReader import ConfigsReader
from fileReader import FileReader
from Analyzer import AnalyzerWrapper

ConfigsReaderVar = ConfigsReader()

def menu():
    print("\nPlease,select an option: \n1. Print list of FIDs with problems;\n2. See diff for the specific FID;\n3. Enter FID to be deleted from analysis\n4. Stop execution of the program;\n")

def main(filename):
        #TODO: AcceptableGeneralSpecializedListVar = deque(ConfigsReaderVar.getAcceptableSpecialysedMismatchList())

        AnalyzerWrapperVar = AnalyzerWrapper(
            FileReader(filename).getDataForAnalysis(),
            deque(ConfigsReaderVar.getAcceptableGeneralMismatchList()),
            list(ConfigsReaderVar.getFIDsNotToBeAnalyzed())
        )

        # while 1:
            #TODO: exception for main
            # menu()
            # option = input()
        AnalyzerWrapperVar.execute_option(1)
            # continue


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage details: please add filename and ContextID.")
        sys.exit
        #TODO len(sys.argv) != 3
    elif len(sys.argv) != 2:
        print("Usage details: parameters are filename and ContextID.")
        sys.exit
    else:
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