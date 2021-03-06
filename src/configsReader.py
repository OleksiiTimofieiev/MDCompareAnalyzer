#!/usr/bin/python

import json
from collections import deque


class ConfigsReader:
    fileName = './config/config.json'
    acceptedGeneral = deque()
    acceptedSpecialized = deque()
    FIDsNotToBeAnalyzed = []

    def __init__(self):
        f = open(self.fileName)
        self.data = json.load(f)
        f.close()

        for x in self.data['generalAcceptableMismatch']:
            sublist = [x['SRC1'], x['SRC2']]
            self.acceptedGeneral.append(sublist)

        for x in self.data['specializedAcceptableMismatch']:
            sublist = [x['FID'], x['SRC1'], x['SRC2']]
            self.acceptedSpecialized.append(sublist)

        for x in self.data['FIDsNotToBeAnalyzed']:
            self.FIDsNotToBeAnalyzed.append(x)

    def getAcceptableGeneralMismatchList(self):
        return self.acceptedGeneral;

    def getAcceptableSpecialysedMismatchList(self):
        return self.acceptedSpecialized;

    def getFIDsNotToBeAnalyzed(self):
        return self.FIDsNotToBeAnalyzed;
