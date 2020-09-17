#language : python 3
#author : C. Martin, U. EB-LEVADOUX
#version : 1.0
#date : 13-10-2019
#USAGE : proceed.py

from shutil import copyfile
import os

path = "./Web_gestion/resource/"
path_web = "./Web_alpha/resource/"


id = 0
module = None
navigation = None


def setup_module_txt(filepath):
      global module
      global id
      copy_txt_file(filepath)

      mod = open(path_web+"/module design/texte.module","r")
      buf = mod.read()
      buf = buf.replace("$filepath", "\"" + filepath + "\"")
      buf = buf.replace("$id",str(id))

      module.write(buf)

      mod.close()

def setup_module_img(filename, filepath) :
     global module
     global id
     copy_img_file(filepath)

     mod = open(path_web + "/module design/image.module","r")
     buf = mod.read()
     buf = buf.replace("$filepath", filepath)
     buf = buf.replace("$filename", "\"" + filename + "\"")
     buf = buf.replace("$id",str(id))

     module.write(buf)

     mod.close()


def setup_module_chart():
    global module
    global id

    mod = open(path_web + "/module design/graphique.module","r")
    buf = mod.read()
    buf = buf.replace("$id",str(id))

    module.write(buf)

    mod.close()


def setup_module_info():
	None


def setup_nav(filename):
    global navigation
    global id

    nav = open(path_web + "/navigation/classique.navigation","r")
    buf = nav.read()
    buf = buf.replace("$filename", filename)
    buf = buf.replace("$id",str(id))

    navigation.write(buf)

    nav.close()


def init():
    global module
    global navigation
    global id

    id = 0

    module = open(path_web + "html/component/module", "w")

    module.write("")
    module.close()
    module = open(path_web + "html/component/module", "a")

    navigation = open(path_web + "html/component/navigation", "w")
    navigation.write("")
    navigation.close()
    navigation = open(path_web + "html/component/navigation", "a")


def copy_txt_file(filepath):
    destination_file_path = path_web + "/txt/"+ filepath
    source_file_path = path + filepath

    copyfile(source_file_path, destination_file_path)


def copy_img_file(filepath):
    destination_file_path = path_web + "/img/"+ filepath
    source_file_path = path + filepath

    copyfile(source_file_path, destination_file_path)



def main():
    global id

    init()

    configuration = open("./Web_gestion/configuration.txt")

    nav = False
    for line in configuration:
      id += 1
      if(line.startswith('(texte)')):
        filename = line[7:].lstrip().rstrip()[:]

        if (filename.endswith('(nav)')) :
            nav = True
            filename = filename[:-5].lstrip().rstrip()[:]

        filepath = filename
        if (filepath[-4:] != ".txt"):
            filepath = filepath + ".txt"
        else :
            filename = filename[:-4]

        setup_module_txt(filepath)

      elif(line.startswith('(image)')):
        filename = line[7:].lstrip().rstrip()[:]

        if (filename.endswith('(nav)')) :
            nav = True
            filename = filename[:-5].lstrip().rstrip()[:]


        filepath = filename
        if (filepath[-4:] != ".jpg"):
            filepath = filepath + ".jpg"
        else :
            filename = filename[:-4]

        setup_module_img(filename, filepath)


      elif(line.startswith('(graphique)')):
        if (filename.endswith('(nav)')) :
            filename = "Graphique"
            nav = True

        setup_module_chart()

          
      elif(line.startswith('(information)')):
        setup_module_info()

      if(nav) :
        setup_nav(filename)
        nav = False

main()

module.close()
navigation.close()
