#Class to create Workers
from person import Person

class Workers(Person):
    def __init__(self,position,salary,name,age,sex,nationality):
        super().__init__(name,age,sex,nationality)
        self.position = position
        self.salary = salary
        self.list = {
            "Worker":{"person":[]}
        }

    def Add_Worker(self,Employee):
        self.list["Worker"].get("person").append(Employee)
        print("Added new employee")