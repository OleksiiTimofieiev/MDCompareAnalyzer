import re

RIC = 1
FID = 3
IDN = 4
ERT = 5
FLAG = 6


def checkIfFormatting(ERT_local, IDN_local):
    try:
        ERT_local_var = re.sub('[""]', '', ERT_local)
        IDN_local_var = re.sub('[""]', '', IDN_local)

        if IDN != 'null' and ERT != 'null':
            if ERT != IDN and float(ERT_local_var) == float(IDN_local_var):
                return True
    except:
        return False


def checkIfSpacingIsAcceptable(IDN_local, ERT_local):
    length_ERT = len(ERT_local)
    length_IDN = len(IDN_local)

    if (length_ERT + IDN_local.count(' ')) == length_IDN and length_IDN != 1:
        # print(IDN_local + " " + ERT_local)
        return True
    return False

def checkIfAcceptableMismatch(IDN_local, ERT_local, AcceptableGeneralMismatch):
    ERT_local_var = re.sub('[""]', '', ERT_local)
    IDN_local_var = re.sub('[""]', '', IDN_local)

    if IDN_local_var == AcceptableGeneralMismatch[0][0] and ERT_local_var == \
            AcceptableGeneralMismatch[0][1]:
        return True
    return False


class Analyzer:
    dictVar = {}
    dictVarQuantityOfMismatches = {}

    def __init__(self, Data_to_analyze, AcceptableGeneralMismatch, FIDsNotToBeAnalyzed):
        self.list_of_fids_with_mismatch = []

        for row in Data_to_analyze:
            lineToAnalyze = row.split(",")

            if lineToAnalyze[FLAG] == '!' and lineToAnalyze[FID] not in FIDsNotToBeAnalyzed:
                if checkIfAcceptableMismatch(lineToAnalyze[IDN], lineToAnalyze[ERT], AcceptableGeneralMismatch):
                    continue
                else:
                    if not checkIfFormatting(lineToAnalyze[IDN], lineToAnalyze[ERT]) and \
                            checkIfSpacingIsAcceptable(lineToAnalyze[IDN], lineToAnalyze[ERT]) != True:

                        if lineToAnalyze[FID] not in self.list_of_fids_with_mismatch:
                            self.list_of_fids_with_mismatch.append(lineToAnalyze[FID])
                            self.dictVar[lineToAnalyze[FID]] = []
                            self.dictVarQuantityOfMismatches[lineToAnalyze[FID]] = 0

                        sublist = [lineToAnalyze[RIC], lineToAnalyze[IDN], lineToAnalyze[ERT]]
                        self.dictVar[lineToAnalyze[FID]].append(sublist)
                        self.dictVarQuantityOfMismatches[lineToAnalyze[FID]] = self.dictVarQuantityOfMismatches[
                                                                                   lineToAnalyze[FID]] + 1

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
            # TODO: list of available options: 1 - FID, differnt function for convertion
            option = input("Please, enter FID for analysis.\n")
            return self.AnalyzerVar.getDetailsOnMismatchesForFID(option)
        except:
            print("Please, valid FID from options list should be selected.")

    def option_3(self):
        return quit()
