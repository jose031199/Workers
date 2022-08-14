# Main Menu to add Workers in Company
from workers import Workers
def Menu():
    is_exit = False
    w1 = Workers()
    list_workers = w1.Create_List()
    while is_exit is not True:
        try:
            options = int(input("Welcome to Work Company \n" +
                            "1. Add Worker \n" +
                            "2. Show Workers \n" +
                            "3. Find Workers by Name \n" +
                            "4. Remove Workers by Name\n" +
                            "5. Exit"
                            " Choose option: "))

        # Options for Menu
            if options == 1:
                try:
                    name = input("Type your name: ").lower()
                    age = int(input("Type your age:"))
                    if w1.IsUnderAge(age) is True:
                        sex = input("Choose an sex M = male F= female: ").lower()
                        if w1.IsMale_Female(sex) is True:
                            nation = input("Type your country:").lower()
                            position = input('Type your position:').lower()
                            salary = float(input('Type your salary:'))
                            worker = Workers(position, salary, name, age, sex, nation)
                            worker.Add_Worker(list_workers)
                        else:print("Is male or female")
                    else:
                        print(f"You must be 18 years or older")
                except Exception as e:
                    print(f"{e}")

            elif options == 2:
                if len(list_workers.get("Workers").get("name"))>0:
                    w1.Show_Employee(list_workers)
                else:
                    print("There is not employees")

            elif options == 3:
                if len(list_workers.get("Workers").get("name"))>0:
                    name = input("Name to search: ")
                    w1.Find_By_Name(name,list_workers)
                else:
                    print("There is not employees")

            elif options == 4:
                if len(list_workers.get("Workers").get("name"))>0:
                    w1.Remove_By_Name(name,list_workers)
                else:
                    print("There is not employees")

            elif options == 5:
                w1.Remove_File()
                print("GoodBye")
                is_exit = True
        except ValueError as e:
            print(f"{e}")
            Menu()


Menu()
