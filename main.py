#!/usr/bin/python
import sys
from collections import deque

from configsReader import ConfigsReader
from fileReader import FileReader


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
        FileReaderVar = FileReader(filename)
        Data_to_analyze = FileReaderVar.getDataForAnalysis()

        list_of_fids_with_mismatch = []

        for x in Data_to_analyze:
            lineToAnalyze = x.split(",")
            # print(x + '\n')
            if lineToAnalyze[6] == '!':
                # print(lineToAnalyze[1] + " " + lineToAnalyze[3] + " " + lineToAnalyze[4] + " " + lineToAnalyze[5] + " " + lineToAnalyze[6])
                if lineToAnalyze[3] not in list_of_fids_with_mismatch:
                    list_of_fids_with_mismatch.append(lineToAnalyze[3])

        for x in list_of_fids_with_mismatch:
            print(x + '\n')
        print("finished")

        while 1:
            continue


if __name__ == "__main__":
    main(sys.argv[1])
# _, a, b = sys.argv
# for filename
# except Exeptioin as e:
# 	print(type(e))
