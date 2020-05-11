#!/usr/bin/python
import sys
from collections import deque

from configsReader import ConfigsReader

ConfigsReader = ConfigsReader()

AcceptableMismatchList = deque(ConfigsReader.getAcceptableMismatchList())

# print(AcceptableMismatchList)

def main():
    if len(sys.argv) == 1:
        print("Usage details: please add filename.")
        sys.exit
    elif len(sys.argv) > 2:
        print("Usage details: only on file can be selected.")
        sys.exit
    else:
        while 1:
            continue

if __name__ == "__main__":
    main()
