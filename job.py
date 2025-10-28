class Job:
    def __init__(self, name=str, category=str, rate=float, date=str, hours=int):
        self.name = name
        self.category = category
        self.rate = rate
        self.date = date
        self.hours = hours

    def get_name(self):
        """gets the name of the worker (str)"""
        try:
            return self.name
        except TypeError:
            print("wrong datatype")
        except AttributeError:
            print("Error: no attribute")
    def get_category(self):
        """gets the category of worker (str)"""
        try:
            return self.category
        except TypeError:
            print("wrong datatype")
        except AttributeError:
            print("Error: no attribute")
    def get_rate(self):
        """gets the hourly rate of worker (float)"""
        try:
            return self.rate
        except TypeError:
            print("wrong datatype")
        except AttributeError:
            print("Error: no attribute")
    def get_date(self):
        """gets the date the worker started (str)"""
        try:
            return self.date
        except TypeError:
            print("wrong datatype")
        except AttributeError:
            print("Error: no attribute")
    def get_hours(self):
        """gets the amount of hours they work a week (int)"""
        try:
            return self.hours
        except TypeError:
            print("wrong datatype")
        except AttributeError:
            print("Error: no attribute")
    def __eq__(self, other):
        try:
            return self.__hash__() == other.__hash__()
        except TypeError:
            print("Error: Type error")
    def __hash__(self):
        return hash(self.name)
    def __str__(self):
        return f"{self.name},{self.category},£{self.rate} an hour,{self.date},works {self.hours} a day"
    def __repr__(self):
        return f"{self.name},{self.category},{self.rate},{self.date},{self.hours}"
