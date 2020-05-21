#!/usr/bin/python
import sys
from collections import deque

from configsReader import ConfigsReader
from fileReader import FileReader
from Analyzer import Analyzer


# print(AcceptableMismatchList)

def main(filename):
    if len(sys.argv) == 1:
        print("Usage details: please add filename.")
        sys.exit
    elif len(sys.argv) > 2:
        print("Usage details: only on file can be selected.")
        sys.exit
    else:
        ConfigsReaderVar = ConfigsReader()
        AcceptableMismatchList = deque(ConfigsReaderVar.getAcceptableMismatchList())
        print(AcceptableMismatchList[0])
        FileReaderVar = FileReader(filename)
        Data_to_analyze = FileReaderVar.getDataForAnalysis()
        AnalyzerVar = Analyzer()

        AnalyzerVar.getListOfFIDWithMismatch(Data_to_analyze, AcceptableMismatchList)

        print("finished")

        while 1:
            continue


if __name__ == "__main__":
    main(sys.argv[1])
# _, a, b = sys.argv
# for filename
# except Exeptioin as e:
# 	print(type(e))
