#Class to create Workers
from person import Person
import json

class Workers(Person):
    def __init__(self,position='',salary=0,name='',age=0,sex='',nationality=''):
        super().__init__(name,age,sex,nationality)
        self.position = position
        self.salary = salary

    def Add_Worker(self,list):
        list["Workers"].get("name").append(self.name)
        list["Workers"].get("age").append(self.age)
        list["Workers"].get("sex").append(self.sex)
        list["Workers"].get("country").append(self.nationality)
        list["Workers"].get("position").append(self.position)
        list["Workers"].get("salary").append(self.salary)
        print(f'Added new employee {list["Workers"].get("name")[0]}')

    def Show_Employee(self,list):
        for key,value in list["Workers"].items():
            print(f"{key}: {value}")

    def Find_By_Name(self,name,list):
        if name in list["Workers"].get("name"):
            index = list["Workers"].get("name").index(name)
            print(f"Name: {list['Workers']['name'][index]}")
            print(f"Age: {list['Workers']['age'][index]}")
            print(f"Position: {list['Workers']['position'][index]}")
            print(f"Country: {list['Workers']['country'][index]}")
            print(f"Salary: {list['Workers']['salary'][index]}")
        else:
            print("No hay ninguna persona con ese nombre")

    def Remove_By_Name(self,name,list):
        if name in list["Workers"].get("name"):
            index = list["Workers"].get("name").index(name)
            list['Workers']['name'].pop(index)
            list['Workers']['age'].pop(index)
            list['Workers']['position'].pop(index)
            list['Workers']['country'].pop(index)
            list['Workers']['sex'].pop(index)
            list['Workers']['salary'].pop(index)
        else:
            print("No hay ninguna persona con ese nombre")

    def Add_File(self):
        try:
            worker_file = open("worker.txt","w")
            worker_file.write()
        except Exception as e:
            print(f"{e} file not created")



    def Create_List(self):
        list_workers = {
            "Workers":{
                "name":[],
                "age":[],
                "sex":[],
                "country":[],
                "position":[],
                "salary":[]
            }
        }


        return list_workers