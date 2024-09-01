import diamondParametersError as d
class Diamond():
    def __init__(self, price, carat, cut, color, clarity, x, y, z, depth, table):
        if(price>325 and price<18,824):
            self.price=price
        else:
            raise d.DiamondParametersError("the price isn't in the range")
        if (carat>0.1 and carat<5.02):
            self.carat=carat
        else:
            raise d.DiamondParametersError("the carat isn't in the range")
        if (cut=="Fair" or cut=="Good", cut=="Very Good", cut=="Premium", cut=="Ideal"):
            self.cut=cut
        else:
            raise d.DiamondParametersError("the cut isn't exist")
        if(color=='D' or color=='E' or color=='F' or color=='G' or color=='H' or color=='I' or color=='J'):
            self.color=color
        else:
            raise d.DiamondParametersError("the color isn't exist")
        if(clarity=='I1' or clarity=='SI2'or clarity=='SI1' or clarity=='VS2' or clarity=='VS1' or clarity=='VVS2' or clarity=='VVS1' or clarity=='IF'):
            self.clarity=clarity
        else:
            raise d.DiamondParametersError("the clarity is invalid")
        if(x>0 and x<10.74):
            self.x=x
        else:
            raise d.DiamondParametersError("the x isn't in the range")
        if(y>0 and x<58.9):
            self.y=y
        else:
            raise d.DiamondParametersError("the y isn't in the range")
        if(z>0 and z<31.8):
            self.z=z
        else:
            raise d.DiamondParametersError("the z isn't in the range")
        self.depth = 2 * self.z / (self.x + self.y)
        self.table = table


    def calculateVolume(self):
        return self.x * self.y * self.z

    def displayInfo(self):
        print("The diamond: price-", self.price, " carat-", self.carat, " cut-", self.cut, " color-",
              self.color, " clarity-"
              , self.clarity, " volume-", self.calculateVolume(), " depth-", self.depth, " table-", self.table)

    def getTablePercentage(self):
        table_percentage= (self.table / max(self.x, self.y)) * 100
        return table_percentage

    def isHighQuality(self):
        if self.clarity=='I1' or self.clarity=='IF':
            return  True
        return  False