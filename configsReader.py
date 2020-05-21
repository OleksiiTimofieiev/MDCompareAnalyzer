#!/usr/bin/python

import json
from collections import deque


class ConfigsReader:
    fileName = 'config.json'
    acceptedMismatch = deque()
    writeResultsToFile = False
    writeResultsToExcel = False

    def __init__(self):
        f = open(self.fileName)
        self.data = json.load(f)
        f.close()

        for x in self.data['generalAcceptableMismatch']:
            sublist = [x['SRC1'], x['SRC2']]
            self.acceptedMismatch.append(sublist)

        for x in self.data['specializedAcceptableMismatch']:
            sublist = [x['FID'], x['SRC1'], x['SRC2']]
            self.acceptedMismatch.append(sublist)

        self.writeResultsToFile = self.data['writeResultsToFile']
        self.writeResultsToExcel = self.data['writeResultsToExcel']

    def getAcceptableMismatchList(self):
        return self.acceptedMismatch;

    def getWriteResultsToFile(self):
        return self.writeResultsToFile;

    def getWriteResultsToExcel(self):
        return self.writeResultsToExcel;
