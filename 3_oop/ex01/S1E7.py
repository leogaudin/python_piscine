from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, is_alive=True):
        """Constructor for Baratheon"""
        super().__init__(first_name=name, family_name='Baratheon',
                         eyes='brown', hairs='dark', is_alive=is_alive)

    def die(self):
        """Method for killing Baratheon"""
        super().die()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, name, is_alive=True):
        """Constructor for Lannister"""
        super().__init__(first_name=name, family_name='Lannister',
                         eyes='blue', hairs='light', is_alive=is_alive)

    def die(self):
        """Method for killing Lannister"""
        super().die()

    @staticmethod
    def create_lannister(name, is_alive):
        """Static method for creating Lannister"""
        return Lannister(name, is_alive)