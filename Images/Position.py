class Position:
    def _init_(self, P: int):
        self.pos = P

    def getPos(self) -> Position: # type: ignore
        return self.pos