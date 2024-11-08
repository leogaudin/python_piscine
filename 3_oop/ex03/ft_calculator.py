class calculator:
    def __init__(self, vector) -> None:
        """Constructor for the Calculator"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Method for summing another vector to the current one"""
        self.vector = [(cell + object) for cell in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Method for multiplying another vector to the current one"""
        self.vector = [(cell * object) for cell in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Method for subtracting another vector to the current one"""
        self.vector = [(cell - object) for cell in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Method for dividing the current vector by another one"""
        try:
            if object == 0:
                raise ValueError('Division by 0')
            self.vector = [(cell / object) for cell in self.vector]
            print(self.vector)

        except Exception as e:
            print(type(e).__name__, ":", e)
