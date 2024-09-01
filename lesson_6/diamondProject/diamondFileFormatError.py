class DiamondFileFormatError(Exception):
    def __init__(self,message="format error"):
        self.message=message
    def __str__(self):
        return (repr(self.value))