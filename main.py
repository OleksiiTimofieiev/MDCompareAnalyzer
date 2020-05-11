#!/usr/bin/python
from collections import deque

from configsReader import ConfigsReader

ConfigsReader = ConfigsReader()

AcceptableMismatchList = deque(ConfigsReader.getAcceptableMismatchList())

# print(AcceptableMismatchList)

def main():
    while 1:
        continue


if __name__ == "__main__":
    main()
