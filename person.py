# Class to create person object

class Person:
    def __init__(self,name,age,sex,nationality):#Method to create a Person
        self.name = name
        self.age = age
        self.sex = sex
        self.nationality = nationality

    def IsUnderAge(self):#Method to know if person person is above 18 can have a job
        if self.age > 18:
            return True