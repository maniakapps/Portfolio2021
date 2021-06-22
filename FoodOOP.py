"""
    Food ordering template
"""

class FoodItem:
    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def print(self):
        """
            Prints the object information
        """
        print(self.fat)
        print(self.name)
        print(self.carbs)
        print(self.protein)


if __name__ == '__main__':
    fd = FoodItem()
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    fd.print()
    fd2 = FoodItem(name, fat, carbs, protein)
    fd2.print()
