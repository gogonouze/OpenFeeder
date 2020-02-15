import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def launch_python_script(script, argv = []) :
    cmd = "python "+str(script)
    for arg in argv :
        cmd = cmd+" "+str(arg)

    os.system(cmd) #GROSSE FAILLE ICI SI MAL GERER.. genre script = "help | rm *"

def main_menu():
    cls()
    event = "not define"
    while(not event == "return"):
        print("=-=-=-=-=")
        print("gestion de la [B]ase de données")
        print("gestion du [S]ite internet")
        print("[Q]uitter")
        print("=-=-=-=-=")
        event = input("\nEntrez votre choix :\n")

        if(event.lower() == "b" or event.lower() == "base de données") :
            event_result = "dataBase_menu"
            event = "return"
        elif(event.lower() == "webSite_menu" or event.lower() == "site internet") :
            event_result = "s"
            event = "return"
        elif(event.lower() == "q" or event.lower() == "quitter") :
            event_result = "quit"
            event = "return"
        else :
            event = ("not define")

        cls()
        if(event == "not define") :
            print("=-=-=-=-=")
            print("Veuillez choisir parmis les choix proposés : b, s, q")

    return event_result


def main() :
    cls()
    event = "main_menu"
    while (not event == "quit") :
        if (event == "main_menu") :
            event = main_menu()
            print(event)
        #elif (event == "" ) :

        cls()



    return 0


if (main() != 0) :
        input('\nOpération échouée.\nAppuyez sur ENTRÉE pour terminer...')
input('\nOpération terminée.\nAppuyez sur ENTRÉE pour terminer...')
cls()
