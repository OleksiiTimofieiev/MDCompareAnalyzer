RIC = 1
FID = 3
IDN = 4
ERT = 5
FLAG = 6


class Analyzer:
    def getListOfFIDWithMismatch(self,Data_to_analyze, AcceptableMismatchList):
        list_of_fids_with_mismatch = []

        for row in Data_to_analyze:
            lineToAnalyze = row.split(",")
            # print(x + '\n')
            if lineToAnalyze[6] == '!':
                # print(lineToAnalyze[1] + " " + lineToAnalyze[3] + " " + lineToAnalyze[4] + " " + lineToAnalyze[5] + " " + lineToAnalyze[6])
                # print(AcceptableMismatchList[0][0])
                # print(AcceptableMismatchList[0][1])

                if lineToAnalyze[4] != AcceptableMismatchList[0][0] and lineToAnalyze[5] != AcceptableMismatchList[0][1]:
                    if lineToAnalyze[3] not in list_of_fids_with_mismatch:
                        list_of_fids_with_mismatch.append(lineToAnalyze[3])

        for x in list_of_fids_with_mismatch:
            print(x)
