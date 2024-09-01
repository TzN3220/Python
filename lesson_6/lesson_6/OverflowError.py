class OverflowError(Exception):
    def __init__(self,message="there is no place to more elements"):
        self.message=message
        super().__init__(self.message)
