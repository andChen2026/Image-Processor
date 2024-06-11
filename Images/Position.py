class Position:
    def _init_(self, P: list):
        self.pos: list = [] # Row, Column #

    def getPos(self) -> Position: # type: ignore
        return self.pos
    
    def setPos(self, P:list) -> None: 
        self.pos = P