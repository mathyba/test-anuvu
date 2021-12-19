"""Tracker models
"""
import abc

class DataStrategy(abc.ABCMeta):

    @abc.abstractproperty
    @property
    def validate(self, data):
        """Validate data"""

    @abc.abstractproperty
    @property
    def description():
        """Short description of dataset requirements."""


class DefaultStrategy(DataStrategy):

    @staticmethod
    def validate(data):
        return isinstance(data, list)

    @property
    def description(self):
        return "A list of undefined items."


class GenericTracker:
    """Base model for tracking a dataset.
    
    Attributes:
        _items (list): dataset
    """

    def __init__(self):
        self.items = []

    @property
    def data_strategy(self):
        return DefaultStrategy


    def insert(self, items):
        """Add items to tracker dataset.
        
        Args:
            items: list of integer values

        Raises:
            ValueError: if input is not a list of integers
        """        
        if not self.data_strategy.validate(items):
            raise ValueError("Data provided is incorrect, expected", expected)

        self.items = items 

    @property
    def mean(self):
        """Get the mean value of the tracker dataset."""
        if not self.items:
            return None
        try:
            return round(float(sum(self.items)) / len(self.items), 2)
        except ValueError:
            raise ValueError("Types in dataset don't allow mean computation")
