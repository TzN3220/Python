import csv

import diamond, diamondFileFormatError as dff, diamondFileNotFoundError as dfnf
class DiamondManager():
    def __init__(self):
        self.l=[]
    def addDiamond(self,diamond:diamond):
        self.l.append(diamond)
    def displayDiamondInfo(self,index):
        self.l[index].displayInfo()
        print("HighQuality",self.l[index].isHighQuality())
        print("TablePercentage",self.l[index].getTablePercentage)
    def fromCSV(self):
        with open("diamonds.csv",'r') as f:
            if f==None:
                raise dfnf.DiamondFileFormatError("file not found")
            read=csv.reader((f))
            try:
                d=list(read)
                return d
            except dff.DiamondFileFormatError as e:
                print("error->" ,e)







