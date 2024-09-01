class DiamondParametersError(Exception):
    def __init__(self,message="The parameter is invalid"):
        self.message=message
        super().__init__(self.message)


