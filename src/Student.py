# @author Brian Callister
# Written in 2023 for the AMB
# Largely assisted by ChatGPT

class Student:
    def __init__(self, name, height, weight, gender, jacket_preference, pants_preference):
        self.name = name
        self.height = height
        self.weight = weight
        self.gender = gender
        self.jacket_preference = jacket_preference
        self.pants_preference = pants_preference
        self.jacket_num = None
        self.pants_num = None
