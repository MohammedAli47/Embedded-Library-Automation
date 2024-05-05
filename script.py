import os

projects = os.listdir(os.curdir)
temp = []
for project in projects:
    if project.find('.', 0, len(project)) == -1:
        temp.append(project)
index = 1
projects = temp
for project in projects:
    print(str(index) + " " + project)
    index += 1
project_number = int(input("Project number: "))
project_name = projects[project_number - 1]
os.chdir(os.path.abspath(project_name))
try:
    os.listdir(os.path.abspath("LIB"))
except FileNotFoundError:
    print("LIB folder not found, please create it first")
    print(os.path.abspath("LIB"))
    exit(1)
lib_path = os.path.abspath("LIB")

layers = os.listdir(os.curdir)
temp = []
for project in layers:
    if project.find('.', 0, len(project)) == -1:
        temp.append(project)
index = 1
layers = temp
for project in layers:
    print(str(index) + " " + project)
    index += 1
layer_number = int(input("Layer number: "))
layer_name = layers[layer_number - 1]
os.chdir(os.path.abspath(layer_name))

library_name = input("Library name: ")
main_path = os.path.abspath(library_name)
print(main_path)

try:
    os.mkdir(main_path)
except FileExistsError:
    print("Library Already Exists")
    exit(1)

os.chdir(main_path)
interface_file = open("%s_interface.h" % library_name, "w")
interface_file.write("#ifndef %s_INTERFACE_H_\n" % library_name)
interface_file.write("#define %s_INTERFACE_H_\n" % library_name)
interface_file.write('#include "%s/errorTypes.h"\n' % lib_path)
interface_file.write('#include "%s/stdTypes.h"\n' % lib_path)
interface_file.write('#include "../../MCAL/DIO/DIO_interface.h"\n')
interface_file.write('#include "../../MCAL/Timer/Timer_interface.h"\n')
interface_file.write('#include "%s_config.h"\n' % library_name)
interface_file.write('#include "%s_private.h"\n\n\n\n' % library_name)
interface_file.write("#endif\n")
interface_file.close()
config_file = open("%s_config.h" % library_name, "w")
config_file.write("#ifndef %s_CONFIG_H_\n" % library_name)
config_file.write("#define %s_CONFIG_H_\n\n\n\n" % library_name)
config_file.write("#endif\n")
config_file.close()
private_file = open("%s_private.h" % library_name, "w")
private_file.write("#ifndef %s_PRIVATE_H_\n" % library_name)
private_file.write("#define %s_PRIVATE_H_\n\n\n\n" % library_name)
private_file.write("#endif\n")
private_file.close()
program_file = open("%s_program.c" % library_name, "w")
program_file.write('#include "%s/errorTypes.h"\n' % lib_path)
program_file.write('#include "%s/stdTypes.h"\n' % lib_path)
program_file.write('#include "../../MCAL/DIO/DIO_interface.h"\n')
program_file.write('#include "../../MCAL/Timer/Timer_interface.h"\n')
program_file.write('#include "%s_config.h"\n' % library_name)
program_file.write('#include "%s_private.h"\n\n\n\n' % library_name)
program_file.close()
print(os.listdir(os.curdir))
