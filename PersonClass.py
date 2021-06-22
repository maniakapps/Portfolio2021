class Person:
    """
        Person model class
    """

    def __init__(self, f, l):
        """
        Person class constructor
        :param f: person first name
        :param l: person last name
        """
        self.f = f
        self.l = l

    def name(self):
        """
        Returns name
        :return: name of person instance
        """
        return self.f + self.l


pO = Person("Marge", "Simpson")
print(pO.name())
