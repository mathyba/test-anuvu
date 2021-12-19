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


class IntegerStrategy(DataStrategy):

    @staticmethod
    def validate(data):
        return all(isinstance(val, int) for val in data)

    @property
    def description(self):
        return "A list of integers."


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
            raise ValueError(
                "Data provided is incorrect, expected", self.data_strategy.description
            )

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


class TemperatureTracker(GenericTracker):
    """Model for tracking temperature data.
    
    Attributes:
        _items (list): dataset
    """

    @property
    def data_strategy(self):
        return IntegerStrategy

    @property
    def min(self):
        """Get min value in tracker dataset.

        Returns:
            None it dataset empty
        """
        if self.items:
            return min(self.items)

    @property
    def max(self):
        """Get max value in tracker dataset.

        Returns:
            None it dataset empty
        """
        if self.items:
            return max(self.items)
