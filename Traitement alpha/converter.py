#language : python 3
#author : C. Martin, U. EB-LEVADOUX
#version : 3.0
#date : 24-01-2020

import os
import sys

destination_filename = "readyForDataBase"

def dialog_create_directory() :
    dialog_check = False
    check = True
    while (check) :
        c = input("Voulez vous créer le dossier ? [o]ui ou [n]on\n")
        if (c.lower() == "o") :
            dialog_check = True
            check = False
        elif (c.lower() == "n") :
            dialog_check = True
            check = False
        else :
            check = True

    return dialog_check


def main() :

    if (len(sys.argv) < 3 ) :
        path, script_name = os.path.split(sys.argv[0])
        print("nombre insuffisant d'arguments.\n<Usage ",script_name," : \"Répertoire source\", \"Répertoire destination\">")
        return 1;
    elif (len(sys.argv) > 3 ) :
        path, script_name = os.path.split(sys.argv[0])
        print("nombre trop important d'arguments.\n<Usage ",script_name," : \"Répertoire source\", \"Répertoire destination\">")
        return 1;

    directory_name = sys.argv[1]
    if (not os.path.isdir(directory_name)) :
        path, script_name = os.path.split(sys.argv[0])
        print("Répertoire source introuvable.\n<Usage ",script_name," : \"Répertoire source\", \"Répertoire destination\">")
        return 2;


    destination_directory = sys.argv[2]
    if (not os.path.isdir(destination_directory)) :
        path, script_name = os.path.split(sys.argv[0])
        print("Répertoire destination introuvable.")
        if (not dialog_create_directory()) :
            print("Répertoire destination introuvable.\n<Usage ",script_name," : \"Répertoire source\", \"Répertoire destination\">")
            return 2;


    raw_contents_paths = raw_directory_files(directory_name)
    process_log_file_list(raw_contents_paths, destination_directory)
    return 0;

def raw_directory_files(directory_name):
    """Renvoie la liste des chemins vers les fichers à traiter"""
    raw_directory = []
    for root, dirs, files in os.walk(directory_name):
        for name in files:
            raw_directory.append(os.path.join(root, name))
        for name in dirs:
            raw_directory_files(os.path.join(root, name))
    return raw_directory

def process_log_file_list(filepath_list, destination_directory):
    """Traite chaque fichier log un à un"""
    if(not os.path.exists(destination_directory)):
        os.mkdir(destination_directory)
    for path in filepath_list:
        log_file = open(path, "r")
        log_filename = log_file.name.lower()
        if(log_filename.endswith('.csv')):
            if('errors' in log_filename):
                None
            elif('rfidfreq'in log_filename):
                None
            elif('udid'in log_filename):
                None
            elif('exttemp'in log_filename):
                None
            elif('firmware'in log_filename):
                None
            elif('timcalib'in log_filename):
                None
            elif('battery'in log_filename):
                None
            else :
                process_log_file(log_file, destination_directory)



        log_file.close()

def process_log_file(log_file, destination_file):
    """Créé un fichier log sans les lignes inutiles"""
    destination_file = open(os.path.join(destination_file, destination_filename), "a+")
    line=' '
    while(line != ''):
        line = log_file.readline()
        if(line.find('XXXXXXXXXX')==-1 and line.find('??????????')==-1):
            destination_file.write(line)
    destination_file.close()

#Global
if (main() > 0) :
    return 0
return 1
