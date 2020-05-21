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

        while 1:
            continue


if __name__ == "__main__":
    main(sys.argv[1])
# _, a, b = sys.argv
# for filename
# except Exeptioin as e:
# 	print(type(e))
