
import numpy as np

class Exam:

    def __init__(self, name, date, concepts):
        print("initalizated")
        self.id = np.random.random_integers(1000)
        self.name = name # name of exam
        self.date = date # num of days before exam
        self.concepts = concepts # concepts of the exam