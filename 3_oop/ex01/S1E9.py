from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for Character"""
    @abstractmethod
    def __init__(self, first_name, family_name,
                 eyes, hairs, is_alive=True):
        """Constructor for Character"""
        self.is_alive = is_alive
        self.first_name = first_name
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    @abstractmethod
    def die(self):
        """Method for killing Character"""
        self.is_alive = False

    def __str__(self):
        """Method for string representation"""
        return str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        """Method for representation"""
        return str((self.family_name, self.eyes, self.hairs))


class Stark(Character):
    """Class for Stark"""
    def __init__(self, name, is_alive=True):
        """Constructor for Stark"""
        super().__init__(first_name=name, family_name='Stark',
                         eyes='blue', hairs='dark', is_alive=is_alive)

    def die(self):
        """Method for killing Stark"""
        super().die()
