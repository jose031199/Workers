# Main Menu to add Workers in Company
from workers import Workers
def Menu():
    is_exit = False
    while is_exit is not True:
        try:
            options = int(input("Welcome to Work Company \n" +
                            "1. Add Worker \n" +
                            "2. Show Workers \n" +
                            "3. Find Workers by Name \n" +
                            "4. Find Workers by Position\n" +
                            "5. Exit"
                            " Choose option: "))

        # Options for Menu
            if options == 1:
                Add_Employee()
                #print("Firs option")
            elif options == 2:
                print("Second option choose")
            elif options == 3:
                print("Third option choose")
            elif options == 4:
                print("Fourth Options Choose")
            elif options == 5:
                print("GoodBye")
                is_exit = True
        except ValueError as e:
            print(f"{e}")
            Menu()

def Add_Employee():
    name = input("Type your name: ").lower()
    age  = int(input("Type your age:"))
    sex = input("Choose an sex M = male F= female: ").lower()
    nation = input("Type your country:").lower()
    position = input('Type your position:').lower()
    salary = float(input('Type your salary:'))
    employee = Workers(position,salary,name,age,sex,nation)
    #print(employee.name)
    employee.Add_Worker(employee)

Menu()
