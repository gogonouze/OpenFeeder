 #language : python 3, SQLite
#author : C. Martin, U. EB-LEVADOUX
#version : 2.0
#date : 31-01-2020

import sqlite3 as sql
import os
import sys

def process_fill_up_db(data_filename, db_filename) :
    conn = sql.connect(db_filename)
    cursor = conn.cursor()

    data ={'date' : None, 'time': None, 'site': None, 'machine': None, 'scenario': None, 'entity': None}
    data_file = open(data_filename,"r")
    for line in data_file :
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
        cursor.execute('insert into ENTITY (Id,IdCaptureSite) select ?,? where not exists(select * from ENTITY where Id=(?))',(data['entity'],data['site'],data['entity'],))

        cursor.execute('select CaptureDate from ENTITY where Id=(?)',(data['entity'],))
        date = cursor.fetchone()[0]

        print(date)
        if date >= data['date'] :
            cursor.execute('update ENTITY set CaptureDate = (?) where Id = (?)', (data['date'],data['entity'],))


        cursor.execute('update ENTITY set IdLastVisitedMachine = (?) where  Id = (?)', (data['machine'],data['entity'],))



    data_file.close()
    data_file = open(data_filename,"w")
    data_file.write("")
    data_file.close()
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

    data_filename = sys.argv[1]
    if (not os.path.isfile(data_filename)) :
        path, script_name = os.path.split(sys.argv[0])
        print("Fichier source introuvable.\n<Usage ",script_name," : \"Fichier source\", \"Base de données déstination\">")
        return 2;


    db_filename = sys.argv[2]
    if (not os.path.isfile(db_filename)) :
        path, script_name = os.path.split(sys.argv[0])
        print("Répertoire destination introuvable.")
        if (not dialog_create_file()) :
            print("Base de données déstination introuvable.\n<Usage ",script_name," : \"Fichier source\", \"Base de données déstination\">")
            return 2;

    process_fill_up_db(data_filename, db_filename)

main()
return 0
