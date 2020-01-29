import os

def launch_python(script, argv) :
    cmd = "python "+str(script)
    for arg in argv :
        cmd = cmd+" "+str(arg)

    os.system(cmd)

launch_python("DataBase_alpha/fill_up_db.py",["DataBase_alpha/readyForDataBase","DataBase_alpha/bddu"])

input('\nOpération terminée.\nAppuyez sur ENTRÉE pour terminer...')
