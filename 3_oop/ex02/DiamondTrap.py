from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, name, is_alive=True):
        """Constructor for King"""
        Lannister.__init__(self, name=name, is_alive=is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Method for killing King"""
        return super().die()

    def set_eyes(self, eyes):
        """Setter for King's eyes"""
        self.eyes = eyes

    def get_eyes(self):
        """Getter for King's eyes"""
        return self.eyes

    def set_hairs(self, hairs):
        """Setter for King's gairs"""
        self.hairs = hairs

    def get_hairs(self):
        """Getter for King's hairs"""
        return self.hairs
