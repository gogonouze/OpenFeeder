#language : python 3
#author : C. Martin, U. EB-LEVADOUX
#version : 2.0
#date : 20-01-2020

import os

destination_filename = "readyForDataBase"

def main() :
    directory_name = input('Répertoire source : ')
    destination_directory = input('Répertoire destination : ')
    raw_contents_paths = raw_directory_files(directory_name)
    process_log_file_list(raw_contents_paths, destination_directory)
    input('\nOpération terminée.\nAppuyez sur ENTRÉE pour terminer...')

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

def process_log_file(log_file, destination_directory):
    """Créé un fichier log sans les lignes inutiles"""
    destination_file = open(os.path.join(destination_directory, destination_filename), "a+")
    line=' '
    while(line != ''):
        line = log_file.readline()
        if(line.find('XXXXXXXXXX')==-1 and line.find('??????????')==-1):
            destination_file.write(line)
    destination_file.close()

#Global
main()
