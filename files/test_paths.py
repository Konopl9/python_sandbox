import os, shutil

for folderName, subfolders, filenames in os.walk(os.getcwd() + '/comple_file'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        if(subfolder == 'more_complex'):
            shutil.copytree(folderName + '/more_complex', folderName + '/more_complex_copy')
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)