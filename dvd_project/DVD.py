import locale
class DVD:
    def __init__(self,title, dvd_type, cost):
        self.title = title
        self.dvd_type = dvd_type
        self.cost = cost

    def setTitle(self, newTitle):
        self.title = newTitle
    def getTitle(self):
        return self.title
    def getType(self):
        return self.dvd_type
    