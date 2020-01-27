#language : python 3, SQLite
#author : C. Martin, U. EB-LEVADOUX
#version : 2.0
#date : 27-01-2020

import sqlite3 as sql
import os
import sys

def process_fill_up_db(file_name, db_name) :
    conn = sql.connect(db_name)
    cursor = conn.cursor()

    data ={'date' : None, 'time': None, 'site': None, 'machine': None, 'scenario': None, 'entity': None}
    file = open(file_name,"r")
    for line in file :
        data_brut = line.split(',')
        print(data_brut)
        print()
        data['date'] = data_brut[0]
        data['time'] = data_brut[1]
        data['site'] = data_brut[2]
        data['machine'] = data_brut[3]
        data['scenario'] = data_brut[4]
        data['entity'] = data_brut[5]

        print(data)
        print()
        cursor.execute('insert into SITE (Id) select ? where not exists(select * from SITE where Id=(?))',(data['site'],data['site'],))
        cursor.execute('insert into MACHINE (Id,IdSite) select ?,? where not exists(select * from MACHINE where Id=(?))',(data['machine'],data['site'],data['machine'],))
        cursor.execute('insert into ENTITY (Id,IdCaptureSite, CaptureDate) select ?,?,? where not exists(select * from ENTITY where Id=(?))',(data['entity'],data['site'],data['date'],data['entity'],))
        cursor.execute('update ENTITY set IdLastVisitedMachine = (?) where  Id = (?)', (data['machine'],data['entity'],))



    file.close()
    file.open(file_name,"w")
    file.write("")
    file.close()
    conn.commit()


def main() :
    if (len(sys.argv) < 3 ) :
        path, script_name = os.path.split(sys.argv[0])
        print("nombre insuffisant d'arguments.\n<Usage ",script_name," : \"Fichier source\", \"Base de données déstination\">")
        return 1;
    elif (len(sys.argv) > 3 ) :
        path, script_name = os.path.split(sys.argv[0])
        print("nombre trop important d'arguments.\n<Usage ",script_name," : \"Fichier source\", \"Base de données déstination\">")
        return 1;

    file_name = sys.argv[1]
    if (not os.path.isdir(directory_name)) :
        path, script_name = os.path.split(sys.argv[0])
        print("Fichier source introuvable.\n<Usage ",script_name," : \"Fichier source\", \"Base de données déstination\">")
        return 2;


    bd_name = sys.argv[2]
    if (not os.path.isdir(destination_directory)) :
        path, script_name = os.path.split(sys.argv[0])
        print("Répertoire destination introuvable.")
        if (not dialog_create_file()) :
            print("Base de données déstination introuvable.\n<Usage ",script_name," : \"Fichier source\", \"Base de données déstination\">")
            return 2;

    process_fill_up_db(file_name, db_name)
    input('\nOpération terminée.\nAppuyez sur ENTRÉE pour terminer...')

main()
