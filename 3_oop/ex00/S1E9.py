from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for Character"""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Constructor for Character"""
        pass

    @abstractmethod
    def die(self):
        """Method for killing Character"""
        pass


class Stark(Character):
    """Class for Stark"""
    def __init__(self, name, is_alive=True):
        """Constructor for Stark"""
        self.name = name
        self.is_alive = is_alive

    def die(self):
        """Method for killing Stark"""
        self.is_alive = False
