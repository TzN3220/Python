class UnderflowError(Exception):
    def __init__(self,message="there is no elements "):
        self.message=message
        super().__init__(self.message)



