#!/usr/bin/python

import sys
from collections import deque

from configsReader import ConfigsReader
from fileReader import FileReader
from Analyzer import AnalyzerWrapper

ConfigsReaderVar = ConfigsReader()

def menu():
    print("\nPlease,select an option: \n1. Print list of FIDs with problems;\n2. See diff for the specific FID;\n3. Enter FID to be deleted from analysis\n4. Stop execution of the program;\n")

def main(filename, CID):
        #TODO: AcceptableGeneralSpecializedListVar = deque(ConfigsReaderVar.getAcceptableSpecialysedMismatchList())

        AnalyzerWrapperVar = AnalyzerWrapper(
            FileReader(filename, CID).getDataForAnalysis(),
            deque(ConfigsReaderVar.getAcceptableGeneralMismatchList()),
            list(ConfigsReaderVar.getFIDsNotToBeAnalyzed()),
            CID
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
    elif len(sys.argv) != 3:
        print("Usage details: parameters are filename and ContextID.")
        sys.exit
    else:
        main(sys.argv[1], sys.argv[2])
