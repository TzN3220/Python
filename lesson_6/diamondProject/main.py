import diamond,diamond_manager as dm, diamondFileNotFoundError, diamondParametersError

diamondManager=dm.DiamondManager()
try:
    diamonds=diamondManager.fromCSV()
except diamondFileNotFoundError.DiamondFileFormatError("the find not found") as e:
    print(e)
for d in diamonds:
    try:
        tmp=diamond.Diamond(float(d[0]),float(d[1]),str(d[2]),str(d[3]),str(d[4]),float(d[5]),float(d[6]),float(d[7]),float(d[8]),float(d[9]))
        diamondManager.addDiamond(tmp)
    except diamondParametersError.DiamondParametersError as e:
        print("error:",e)
i=0
while i<len(diamondManager.l):
    diamondManager.displayDiamondInfo(i)
    i+=1

