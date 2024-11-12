from os import listdir
from os.path import isfile, join, splitext, split

source_directory_path = '/Users/jsheriff/Documents/triumph/rules/print-diagrams'
dest_directory_path = '/Users/jsheriff/Documents/triumph/rules/print-diagrams/eps'
file_list = [f for f in listdir(source_directory_path) if isfile(join(source_directory_path, f))]

with open('convert-to-eps.sh', 'w') as command_file:
    command_file.write('#!/bin/bash\n\n')
    for filename in file_list:
        source_file_path = join(source_directory_path, filename)
        base_name, extension = splitext(source_file_path)
        if extension == '.svg':
            dest_file_path = join (dest_directory_path, split(base_name)[1] + '.eps')
            command = '/Applications/Inkscape.app/Contents/Resources/bin/inkscape ' + source_file_path + ' --export-eps=' + dest_file_path + ' -z'
            command_file.write(command + '\n')
