#!/user/bin/python3
"""
Script to move files from downloads folder, documents to docs folder,
other to misc folder.
"""
import os
import shutil

# Get current user
user = os.getlogin()
os.chdir('/home/' + user + '/Downloads/')
print(os.getcwd())

try:
    # list items in directory
    for i in os.listdir():
        f_name, f_ext = os.path.splitext(i)
        if f_ext == '.pdf' or f_ext == '.docx' or f_ext == '.txt':
            shutil.move(i, '/home/' + user + '/Documents/')
        else:
            shutil.move(i, 'moved/')
    
except OSError:
    print('Was an error')
