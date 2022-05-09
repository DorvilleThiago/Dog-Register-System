from str_functions import Menu,Color,Title,Middle
import sql_functions
from time import sleep

sql_functions.CheckOrCreateDatabase()
sql_functions.SelectDatabase()
sql_functions.CheckOrCreateTable()

options = ["1","2","3","4"]

while True:
    Menu()
    choice = input(f"{Color('Option:','Yellow')} ".rjust(33)).strip()
    if choice not in options:
        print(f"{Color('ERROR! Invalid choice, check our options again','Red')}")
    elif choice == "1":
        sql_functions.ShowAllDogs()
    elif choice == "2":
        name = input("Name: ").strip()
        while True:
            borned_year = input("Borned at (Year): ")
            if borned_year.isnumeric():
                if len(borned_year) == 4:
                    borned_year = int(borned_year)
                    break
                else:
                    print(f"{Color('ERROR! It needs exactly 4 digits','Red')}")
            else:
                print(f"{Color('ERROR! It has to be a number','Red')}")
        while True:
            borned_month = input("Borned at (Month): ")
            if borned_month.isnumeric():
                borned_month = int(borned_month)
                break
            else:
                print(f"{Color('ERROR! It has to be a number','Red')}")
        while True:
            borned_day = input("Borned at (Day): ")
            if borned_day.isnumeric():
                borned_day = int(borned_day)
                break
            else:
                print(f"{Color('ERROR! It has to be a number','Red')}")
        borned_at = "{}-{}-{}".format(borned_year,borned_month,borned_day)
        while True:
            sex = input("Sex: ").strip().upper()
            if sex in "MF":
                break
            else:
                print(f"{Color('ERROR! Invalid choice, Type only M or F','Red')}")
        color = input("Color: ").strip()
        while True:
            fluffyness = input("Fluffiness [Ex: 6.7]: ").strip()
            try:
                float(fluffyness)
            except:
                print(f"{Color('ERROR! It has to be a decimal number, example: 5.2','Red')}")
            else:
                fluffyness = float(fluffyness)  
                break
        sql_functions.AddDog(name,borned_at,sex,color,fluffyness)
        print(f"{Color('DONE! Process ended, dog added successfully','Red')}")
        sleep(1)
    elif choice == "3":
        while True:
            ide = input("Id: ").strip()
            if ide.isnumeric():
                ide = int(ide)
                break
            else:
                print(f"{Color('ERROR! It has to be a number','Red')}")
        sql_functions.DeleteDog(ide)
        print(f"{Color('DONE! Process ended, dog removed successfully','Red')}")
        sleep(1)
    elif choice == "4":
        break
Title("Ending System...")
sql_functions.EndSqlConnection()
sleep(0.5)
Middle("Done!")
