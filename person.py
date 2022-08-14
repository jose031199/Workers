# Class to create person object

class Person:
    def __init__(self,name,age,sex,nationality):#Method to create a Person
        self.name = name
        self.age = age
        self.sex = sex
        self.nationality = nationality

    def IsUnderAge(self,age):#Method to know if person person is above 18 can have a job
        if age > 18:
            return True
    def IsMale_Female(self,sex):#Method to accept only if is male or female
        if sex == 'm' or sex=='f':
            return True