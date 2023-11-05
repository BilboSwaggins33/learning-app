import math
import numpy as np

class Exam:

    def __init__(self, name, date, concepts, confidence, real_date):
        print("initalizated")
        self.id = np.random.random_integers(1000)
        self.name = name # name of exam
        self.date = date # num of days before exam
        self.concepts = concepts # concepts of the exam
        self.confidence = int(confidence)
        self.study_times = []
        self.real_date = real_date


        time = 1
        elapsed_time = 1
        while (elapsed_time <= self.date):
            retention = math.exp(-time / self.confidence)
            if (retention < 0.5): # means need revision
                if (elapsed_time >= date):
                    self.study_times.append(date)
                else:
                    self.study_times.append(elapsed_time)
                print(elapsed_time)
                self.confidence += 1
                time = 1
            elapsed_time += 1
            time += 1
            
        # for time in range (1,22):
        #     retention = math.exp(-time / self.confidence)
        #     if (retention < 0.5): # means need revision
        #         self.study_times.append(time)
        #         self.confidence += 5




    # def get_study_times(confidence):
    #     study_times = []
    #     for time in range (1,20):
    #         retention = math.exp(-time / confidence)
    #         if (retention < 0.5): # means need revision
    #             study_times.append(time)
    #             confidence += 5
