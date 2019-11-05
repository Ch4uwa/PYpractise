#!/user/bin/python3
"""
Script to move files from downloads folder, documents to docs folder,
other to misc folder.
"""
import os
import shutil

# Get current user
user = os.getlogin()
# Change directory
os.chdir('/home/' + user + '/Downloads/')
# Print current working directory
print(os.getcwd())

try: # Try to list directory
    for i in os.listdir():
        # Loop through current working directory
        # and split name and extention into vars
        f_name, f_ext = os.path.splitext(i)
        if f_ext == '.pdf' or f_ext == '.docx' or f_ext == '.txt':
            # move extention specified to documents folder
            try:
                shutil.move(i, '/home/' + user + '/Documents/')
            except IOError as mtde:
                print('ERROR when moving documents')
        else:
            # move all other extetions found to another place
            try:
                shutil.move(i, 'moved/')
            except IOError:
                print('ERROR moving not specified files')

except OSError as e:
    print('OS System call failed')
finally:
    print('Finally statement')
