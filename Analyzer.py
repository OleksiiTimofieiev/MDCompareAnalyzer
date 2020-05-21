RIC = 1
FID = 3
IDN = 4
ERT = 5
FLAG = 6


class Analyzer:
    dictVar = {}

    def __init__(self, Data_to_analyze, AcceptableGeneralMismatch, FIDsNotToBeAnalyzed):
        self.list_of_fids_with_mismatch = []

        for row in Data_to_analyze:
            lineToAnalyze = row.split(",")

            if lineToAnalyze[FLAG] == '!' and lineToAnalyze[FID] not in FIDsNotToBeAnalyzed:
                if lineToAnalyze[IDN] != AcceptableGeneralMismatch[0][0] and lineToAnalyze[ERT] != \
                        AcceptableGeneralMismatch[0][1]:
                    if lineToAnalyze[FID] not in self.list_of_fids_with_mismatch:
                        self.list_of_fids_with_mismatch.append(lineToAnalyze[FID])
                        self.dictVar[lineToAnalyze[FID]] = []

                    sublist = [lineToAnalyze[RIC], lineToAnalyze[IDN], lineToAnalyze[ERT]]
                    self.dictVar[lineToAnalyze[FID]].append(sublist)

    def getListOfFIDWithMismatch(self):
        for MismatchedFID in self.list_of_fids_with_mismatch:
            print(MismatchedFID)
        # print(self.dictVar.keys())

    def getDetailsOnMismatchesForFID(self, SpecifiedFID):
        for MismatchedUpdate in self.dictVar[str(SpecifiedFID)]:
            print(MismatchedUpdate)
        print()
    # RIC IDN ERT
    # use tuple
    # FID# RIC IDN ERT
    # FID - key, RIC IDN ERT
    # write to file


class Switcher(object):

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
        #TODO: exception for the invalid key
        option = input("Please, enter FID for analysis.\n")
        #TODO: list of available options
        return self.AnalyzerVar.getDetailsOnMismatchesForFID(option)

    def option_3(self):
        return quit()
