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
            sublist = []
            sublist.append(x['FID'])
            sublist.append(x['SRC1'])
            sublist.append(x['SRC2'])
            self.acceptedMismatch.append(sublist)
            
        for x in self.data['specializedAcceptableMismatch']:
            sublist = []
            sublist.append(x['FID'])
            sublist.append(x['SRC1'])
            sublist.append(x['SRC2'])
            self.acceptedMismatch.append(sublist)
            
        self.writeResultsToFile = self.data['writeResultsToFile']
        self.writeResultsToExcel = self.data['writeResultsToExcel']
        # print(self.acceptedMismatch)
        # print(self.acceptedMismatch[0][0])
        # print(self.acceptedMismatch[0][1])
        # print(self.acceptedMismatch[0][2])
        # print(self.writeResultsToFile)
        # print(self.writeResultsToExcel)
    def getAcceptableMismatchList(self):
        return self.acceptedMismatch;
    def getWriteResultsToFile(self):
        return self.writeResultsToFile;
    def getWriteResultsToExcel(self):
        return self.writeResultsToExcel;
    
# ConfigsReader = ConfigsReader()

# print(ConfigsReader.getWriteResultsToFile())
# print(ConfigsReader.getWriteResultsToExcel())
# print(ConfigsReader.getAcceptableMismatchList())

# deq = deque(ConfigsReader.getAcceptableMismatchList())

# print(deq)