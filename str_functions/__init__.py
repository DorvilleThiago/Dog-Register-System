from time import sleep
colors = {'Yellow':'\033[33m','Blue':'\033[34m','Normal':'\033[37m','Red':'\033[31m'}

def Line():
    print("="*40)

#prints a quick tittle
def Title(text):
    print("="*40)
    print(text.center(40))
    print("="*40)

#prints a centered text
def Middle(text):
    print(text.center(40))

#returns a short colored string
def Color(text='', color='Blue'): 
    return f"{colors[color]}{text}{colors['Normal']}"

#prints a quick option
def Option(number, option):
    sleep(0.1)
    print(f"{Color('[','Blue')}{Color(number,'Yellow')}{Color(']','Blue')} {Color(option,'Yellow')}")


#gives the main menu to the user
def Menu():
    Title("Dog Register System")
    Option("1", "Show All Dogs")
    Option("2", "Add New Dog")
    Option("3", "Remove Dog")
    Option("4", "Quit")