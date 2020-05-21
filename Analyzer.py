RIC = 1
FID = 3
IDN = 4
ERT = 5
FLAG = 6

class Analyzer:
    def getListOfFIDWithMismatch(self, Data_to_analyze, AcceptableMismatchList, FIDsNotToBeAnalyzed):
        list_of_fids_with_mismatch = []

        for row in Data_to_analyze:
            lineToAnalyze = row.split(",")

            if lineToAnalyze[FLAG] == '!' and lineToAnalyze[FID] not in FIDsNotToBeAnalyzed:
                if lineToAnalyze[IDN] != AcceptableMismatchList[0][0] and lineToAnalyze[ERT] != AcceptableMismatchList[0][1]:
                    if lineToAnalyze[FID] not in list_of_fids_with_mismatch:
                        list_of_fids_with_mismatch.append(lineToAnalyze[FID])

        for x in list_of_fids_with_mismatch:
            print(x)


class Switcher(object):
    AnalyzerVar = Analyzer()

    def __init__(self, Data_to_analyze, AcceptableMismatchList, FIDsNotToBeAnalyzed):
        self.Data_to_analyze = Data_to_analyze
        self.AcceptableMismatchList = AcceptableMismatchList
        self.FIDsNotToBeAnalyzed = FIDsNotToBeAnalyzed

    def execute_option(self, argument):
        method_name = 'option_' + str(argument)
        method = getattr(self, method_name, lambda: "Invalid month")
        return method()

    def option_1(self):
        return self.AnalyzerVar.getListOfFIDWithMismatch(self.Data_to_analyze, self.AcceptableMismatchList, self.FIDsNotToBeAnalyzed)

    def option_2(self):
        return quit()

    def option_3(self):
        return "March"
