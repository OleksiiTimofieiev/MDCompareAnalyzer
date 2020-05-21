import re

RIC = 1
FID = 3
IDN = 4
ERT = 5
FLAG = 6

def checkIfFormatting(ERT, IDN):
    try:
        ERT_local = re.sub('[""]', '', ERT)
        IDN_local = re.sub('[""]', '', IDN)

        if IDN != 'null' and ERT != 'null':
            if ERT != IDN and float(ERT_local) == float(IDN_local):
                return True
    except:
        return False


class Analyzer:
    dictVar = {}
    dictVarQuantityOfMismatches = {}

    def __init__(self, Data_to_analyze, AcceptableGeneralMismatch, FIDsNotToBeAnalyzed):
        self.list_of_fids_with_mismatch = []

        for row in Data_to_analyze:
            lineToAnalyze = row.split(",")

            if lineToAnalyze[FLAG] == '!' and lineToAnalyze[FID] not in FIDsNotToBeAnalyzed:
                if lineToAnalyze[IDN] != AcceptableGeneralMismatch[0][0] and lineToAnalyze[ERT] != \
                        AcceptableGeneralMismatch[0][1]:
                    if not checkIfFormatting(lineToAnalyze[IDN], lineToAnalyze[ERT]):
                        if lineToAnalyze[FID] not in self.list_of_fids_with_mismatch:
                            self.list_of_fids_with_mismatch.append(lineToAnalyze[FID])
                            self.dictVar[lineToAnalyze[FID]] = []
                            self.dictVarQuantityOfMismatches[lineToAnalyze[FID]] = 0

                        sublist = [lineToAnalyze[RIC], lineToAnalyze[IDN], lineToAnalyze[ERT]]
                        self.dictVar[lineToAnalyze[FID]].append(sublist)
                        self.dictVarQuantityOfMismatches[lineToAnalyze[FID]] = self.dictVarQuantityOfMismatches[lineToAnalyze[FID]] + 1

    def getListOfFIDWithMismatch(self):
        for MismatchedFID in self.list_of_fids_with_mismatch:
            print(MismatchedFID + " - " + str(self.dictVarQuantityOfMismatches[MismatchedFID]))

    def getDetailsOnMismatchesForFID(self, SpecifiedFID):
        for MismatchedUpdate in self.dictVar[str(SpecifiedFID)]:
            print(MismatchedUpdate)


class AnalyzerWrapper(object):

    def __init__(self, Data_to_analyze, AcceptableGeneralMismatch, FIDsNotToBeAnalyzed):
        self.Data_to_analyze = Data_to_analyze
        self.AcceptableGeneralMismatch = AcceptableGeneralMismatch
        self.FIDsNotToBeAnalyzed = FIDsNotToBeAnalyzed
        self.AnalyzerVar = Analyzer(Data_to_analyze, AcceptableGeneralMismatch, FIDsNotToBeAnalyzed)

    def execute_option(self, argument):
        method_name = 'option_' + str(argument)
        method = getattr(self, method_name, lambda: "Invalid option")
        return method()

    def option_1(self):
        return self.AnalyzerVar.getListOfFIDWithMismatch()

    def option_2(self):
        try:
            #TODO: list of available options: 1 - FID, differnt function for convertion
            option = input("Please, enter FID for analysis.\n")
            return self.AnalyzerVar.getDetailsOnMismatchesForFID(option)
        except:
            print("Please, valid FID from options list should be selected.")

    def option_3(self):
        return quit()
