import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def launch_python_script(script, argv = []) :
    cmd = "python3 "+str(script)
    for arg in argv :
        cmd = cmd+" "+str(arg)

    os.system(cmd) #GROSSE FAILLE ICI SI MAL GERE.. genre : script = "help | rm *"

def main_menu(): #dataBase_menu, webSite_menu, quit
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
        elif(event.lower() == "s" or event.lower() == "site internet") :
            event_result = "webSite_menu"
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

def webSite_menu(): #webSite_configuration, webSite_update, main_menu
    cls()
    event = "not define"
    while(not event == "return"):
        print("=-=-=-=-=")
        print("[C]onfigurer le site internet")
        print("[M]ettre à jours le site internet")
        print("[R]evenir")
        print("=-=-=-=-=")
        event = input("\nEntrez votre choix :\n")

        if(event.lower() == "c" or event.lower() == "configurer le site internet" or event.lower() == "configurer") :
            event_result = "webSite_configuration"
            event = "return"
        elif(event.lower() == "m" or event.lower() == "mettre à jours le site internet " or event.lower() == "mettre à jours") :
            event_result = "webSite_update"
            event = "return"

        elif(event.lower() == "r" or event.lower() == "revenir") :
            event_result = "main_menu"
            event = "return"

        else :
            event = "not define"

        cls()
        if(event == "not define") :
            print("=-=-=-=-=")
            print("Veuillez choisir parmis les choix proposés : c, m, r") # NOTE: a modifier soon

    return event_result

def dataBase_menu() : #dataBase_update, dataBase_update, main_menu
    cls()
    event = "not define"
    while(not event == "return"):
        print("=-=-=-=-=")
        print("[T]raiter les données")
        print("[M]ettre à jours la base de données")
        print("[R]evenir")
        print("=-=-=-=-=")
        event = input("\nEntrez votre choix :\n")

        if(event.lower() == "t" or event.lower() == "traiter les données") or  event.lower() =="traiter" :
            event_result = "dataBase_process"
            event = "return"
        elif(event.lower() == "m" or event.lower() == "mettre à jours la base de données" or event.lower() =="mettre à jours") :
            event_result = "dataBase_update"
            event = "return"
        elif(event.lower() == "r" or event.lower() == "revenir") :
            event_result = "main_menu"
            event = "return"

        else :
            event = ("not define")

        cls()
        if(event == "not define") :
            print("=-=-=-=-=")
            print("Veuillez choisir parmis les choix proposés : r") # NOTE: a modifier soon

    return event_result


def main() :
    cls()
    event = "main_menu"
    while (not event == "quit") :
        if (event == "main_menu") :
            event = main_menu()

        elif (event == "webSite_menu") :
            event = webSite_menu()
        elif (event == "webSite_configuration") :
            os.startfile("Web_gestion/configuration.txt") # GRO TEST
            event = "webSite_menu" # TODO : fonction de la configuration du site web
        elif (event == "webSite_update") :
            launch_python_script("Web_gestion/proceed.py")
            event = "webSite_menu"

        elif (event == "dataBase_menu") :
            event = dataBase_menu()
        elif (event == "dataBase_process") :
            launch_python_script("Treatment_alpha/converter.py",["Treatment_alpha/Raw","Treatment_alpha/Processed"])
            event = "dataBase_menu"
        elif (event == "dataBase_update") :
            launch_python_script("DataBase_alpha/updateDataBase.py",["Treatment_alpha/Processed/generalData","DataBase_alpha/dataBase"])
            event = "dataBase_menu"


        else :
            print("Evénement inconnu : ",event)
            return 1
        cls()

    return 0


if (main() != 0) :
    input('\nOpération échouée.\nAppuyez sur ENTRÉE pour terminer...')
else :
    input('\nOpération terminée.\nAppuyez sur ENTRÉE pour terminer...')
cls()
