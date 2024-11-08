class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Method for doing a dot product between two vectors"""
        product_sum = [(a * b) for a, b in zip(V1, V2)]
        print(sum(product_sum))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Method for adding two vectors"""
        sums = [(a + b) for a, b in zip(V1, V2)]
        print(sums)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Method for subtracting two vectors"""
        subtractions = [(a - b) for a, b in zip(V1, V2)]
        print(subtractions)
