#language : python 3, SQLite
#author : C. Martin, U. EB-LEVADOUX
#version : 1.0
#date : 20-01-2020

import sqlite3 as sql
import os

def dialog_create_file() :
    dialog_check = False
    check = True
    while (check) :
        c = input("Voulez vous créer le fichier ? [o]ui ou [n]on\n")
        if (c.lower() == "o") :
            dialog_check = True
            check = False
        elif (c.lower() == "n") :
            dialog_check = True
            check = False
        else :
            check = True

    return dialog_check


def process_db(sqlite_filename, db_filename) :
    conn = sql.connect(db_filename)
    cursor = conn.cursor()

    file = open(sqlite_filename,"r")
    for line in file :
        cursor.execute(line)

    file.close()

    conn.commit()

def main() :

    check = True
    while (check) :
        sqlite_filename = input('Code sql source : ')
        if (os.path.isfile(sqlite_filename)) :
            check = False
            print("Fichier trouvé")
            print("")
        else :
            check = True
            print("Fichier introuvable")
            print("")

    check = True
    while (check) :
        db_filename = input('Base de donnée destination : ')
        if (os.path.isfile(db_filename)) :
            check = False
            print("Fichier trouvé")
            print("")
        else :
            check = True
            print("Fichier introuvable")
            if (dialog_create_file()) :
                f = open(db_filename,"w")
                f.close()
                check = False

            print("")

    process_db(sqlite_filename, db_filename)
    input('\nOpération terminée.\nAppuyez sur ENTRÉE pour terminer...')

main()
