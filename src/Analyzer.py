import re
import openpyxl

RIC = 1
FID = 3
IDN = 4
ERT = 5
FLAG = 6


def checkIfFormatting(ERT_local, IDN_local):
    try:
        ERT_local_var = re.sub('[""]', '', ERT_local)
        IDN_local_var = re.sub('[""]', '', IDN_local)

        if ERT_local_var != 'null' and IDN_local_var != 'null':
            if ERT_local_var != IDN_local_var and float(ERT_local_var) == float(IDN_local_var):
                return True
    except:
        return False

def checkIfSpacingIsAcceptable(IDN_local, ERT_local):
    length_ERT = len(ERT_local)
    length_IDN = len(IDN_local)

    if (length_ERT + IDN_local.count(' ')) == length_IDN and length_IDN != 1 and IDN_local.count(' ') != 0:
        return True
    return False

#TODO make it universal
def checkIfAcceptableMismatch(IDN_local, ERT_local, AcceptableGeneralMismatch):
    ERT_local_var = re.sub('[""]', '', ERT_local)
    IDN_local_var = re.sub('[""]', '', IDN_local)

    if IDN_local_var == AcceptableGeneralMismatch[0][0] and ERT_local_var == \
            AcceptableGeneralMismatch[0][1]:
        return True
    elif IDN_local_var == AcceptableGeneralMismatch[1][0] and ERT_local_var == \
            AcceptableGeneralMismatch[1][1]:
        return True
    return False

def checkConditions(lineToAnalyze, AcceptableGeneralMismatch):
    if checkIfAcceptableMismatch(lineToAnalyze[IDN], lineToAnalyze[ERT], AcceptableGeneralMismatch):
        return True
    elif checkIfFormatting(lineToAnalyze[IDN], lineToAnalyze[ERT]):
        return True
    elif checkIfSpacingIsAcceptable(lineToAnalyze[IDN], lineToAnalyze[ERT]):
        return True
    return False


class Analyzer:
    dictVar = {}
    dictVarQuantityOfMismatches = {}

    def __init__(self, Data_to_analyze, AcceptableGeneralMismatch, FIDsNotToBeAnalyzed, CID):
        self.list_of_fids_with_mismatch = []
        self.filenameToWrite = 'Result_' + CID + '.xlsx'

        for row in Data_to_analyze:
            lineToAnalyze = row.split(",")

            if lineToAnalyze[FLAG] == '!':
                if lineToAnalyze[FID] not in FIDsNotToBeAnalyzed:
                    if not checkConditions(lineToAnalyze, AcceptableGeneralMismatch):
                        if lineToAnalyze[FID] not in self.list_of_fids_with_mismatch:
                            self.list_of_fids_with_mismatch.append(lineToAnalyze[FID])
                            self.dictVar[lineToAnalyze[FID]] = []
                            self.dictVarQuantityOfMismatches[lineToAnalyze[FID]] = 0

                        sublist = [lineToAnalyze[RIC], lineToAnalyze[IDN], lineToAnalyze[ERT]]
                        self.dictVar[lineToAnalyze[FID]].append(sublist)
                        self.dictVarQuantityOfMismatches[lineToAnalyze[FID]] = self.dictVarQuantityOfMismatches[lineToAnalyze[FID]] + 1
            else:
                continue


    def generateSheetsResultsForFIDs(self):
        wb = openpyxl.load_workbook(filename=self.filenameToWrite)

        sheetnames = wb.get_sheet_names()
        # print(sheetnames)

        for sheet in sheetnames:
            if sheet != 'Sheet':
                wbSheet = wb[sheet]
                dataForSheet = self.dictVar[sheet]
                wbSheet.cell(row=1, column=1).value = "RIC"
                wbSheet.cell(row=1, column=2).value = "IDN"
                wbSheet.cell(row=1, column=3).value = "ERT"
                i = 2
                for singleLine in dataForSheet:
                    wbSheet.cell(row=i, column=1).value = singleLine[0]
                    wbSheet.cell(row=i, column=2).value = singleLine[1]
                    wbSheet.cell(row=i, column=3).value = singleLine[2]
                    i = i + 1
            else:
                wbSheet = wb[sheet]
                wbSheet.cell(row=1, column=1).value = "FID"
                wbSheet.cell(row=1, column=2).value = "Mismatches quantity"
                i = 2
                for MismatchedFID in self.list_of_fids_with_mismatch:
                    wbSheet.cell(row=i, column=1).value = MismatchedFID
                    wbSheet.cell(row=i, column=2).value = self.dictVarQuantityOfMismatches[MismatchedFID]
                    i = i + 1
                wbSheet.title = "Statistics"
        wb.save(filename=self.filenameToWrite)
        wb.close()

    def getListOfFIDWithMismatch(self):
        ws_name = self.filenameToWrite
        rb = openpyxl.load_workbook(ws_name)

        for MismatchedFID in self.list_of_fids_with_mismatch:
            rb.create_sheet(MismatchedFID)

        rb.save(ws_name)
        rb.close()

        self.generateSheetsResultsForFIDs()

    def getDetailsOnMismatchesForFID(self, SpecifiedFID):
        for MismatchedUpdate in self.dictVar[str(SpecifiedFID)]:
            print(MismatchedUpdate)

    def deleteFIDFromAnalysis(self, FIDVar):
        del (self.dictVar[FIDVar])
        del (self.dictVarQuantityOfMismatches[FIDVar])
        self.list_of_fids_with_mismatch.remove(FIDVar)


class AnalyzerWrapper(object):

    def __init__(self, Data_to_analyze, AcceptableGeneralMismatch, FIDsNotToBeAnalyzed, CID):
        self.Data_to_analyze = Data_to_analyze
        self.AcceptableGeneralMismatch = AcceptableGeneralMismatch
        self.FIDsNotToBeAnalyzed = FIDsNotToBeAnalyzed
        self.AnalyzerVar = Analyzer(Data_to_analyze, AcceptableGeneralMismatch, FIDsNotToBeAnalyzed, CID)

    def execute_option(self, argument):
        method_name = 'option_' + str(argument)
        method = getattr(self, method_name, lambda: "Invalid option")
        return method()

    def option_1(self):
        return self.AnalyzerVar.getListOfFIDWithMismatch()

    def option_2(self):
        try:
            # TODO: list of available options: 1 - FID, different function for convertion
            option = input("Please, enter FID for analysis.\n")
            return self.AnalyzerVar.getDetailsOnMismatchesForFID(option)
        except:
            print("Please, valid FID from options list should be selected.")

    def option_3(self):
        try:
            # TODO: list of available options: 1 - FID, different function for convertion
            option = input("Please, enter FID for deletion from analysis.\n")
            return self.AnalyzerVar.deleteFIDFromAnalysis(option)
        except:
            print("Please, valid FID from options list should be selected.")

    def option_4(self):
        return quit()
