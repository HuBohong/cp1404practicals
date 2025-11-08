import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Initialize a Project instance.
        :param name: project name
        :param start_date: start date in d/m/Y format
        :param priority: project priority
        :param cost_estimate: cost estimate
        :param completion_percentage: percentage of completion
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """ Return a string representation of the Project instance. """
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority:{self.priority}, estimate:${self.cost_estimate}, completion:{self.completion_percentage}%"

    def __str__(self):
        """ Return a user-friendly string representation of the Project instance. """
        return f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority:{self.priority}, estimate:${self.cost_estimate}, completion:{self.completion_percentage}%"

    def __lt__(self, other):
        """ Less-than comparison based on start_date. """
        return self.start_date < other.start_date

    def __le__(self, other):
        """ Less-than-or-equal comparison based on start_date. """
        return self.start_date <= other.start_date

    def is_complete(self):
        """ Check if the project is complete. """
        return self.completion_percentage == 100

    def update(self, new_percentage=None, new_priority=None):
        """update the project's completion percentage and priority."""
        self.completion_percentage = new_percentage
        self.priority = new_priority