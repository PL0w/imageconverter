'''
    MY PERSONAL LIBRARY OF FUNCTIONS THAT
    DO BASIC DIRECTORY OPERATIONS. 
'''

from pathlib import Path
import shutil
import os

def check_dir(user_input):
    '''
        Returns user input of dir if it exists    
    '''
    try:
        # user_input = Path(str(input('\nEnter dir path: ')))
        user_input.exists()
        return True    
    except (FileNotFoundError, NotADirectoryError, OSError):
        print("Please enter a directory...\n")  # doesn't reach
        return False

def create_dir(dir):
    '''
        Creates a folder in the cwd
    '''
    try:
        dir_string = str(dir) + f'\\New_Folder\\'
        new_dir = Path(dir_string)
        new_dir.mkdir()
        print('\n****CREATED FOLDER****\n')
        return new_dir
    except FileExistsError:
        print('\n****EXISTING FOLDER****\n')
        return new_dir

def check_img_in_dir(imagepath, dir, dir_list):
    '''
        Checks if img is inside of given dir
    '''
    
    try:
        if imagepath.name in dir_list:
            print(f'\n{imagepath.name} already exists inside {dir.name}')
            return True
    except (FileNotFoundError, NotADirectoryError, TypeError): return False


def create_dir_list(dir):
    ''' 
        Creates specific list of dir
        x.suffix == 'file ext here'
    '''
    dir_list = []
    try:
        [dir_list.append(x.name) for x in dir.iterdir() if x.suffix == '.jpg']
        return dir_list
    except AttributeError: print('\ndirectory list not created')


def change_dir(dir):
    ''' Changes the CWD '''
    os.chdir(dir.as_posix())

def get_cwd():
    ''' Returns the CWD  '''
    return os.getcwd()

def print_cwd():
    ''' Prints the CWD '''
    print(os.getcwd())

def move_img_to_folder(image, dir):
    '''
        Moves img to default folder
    '''
    # dir_string = dir.as_posix() + '\\New_Folder'
    # new_dir = Path(dir_string)
    shutil.move(image, dir)
    print(f'transfered {image} to folder {dir.name}\n')

def print_all_png(dir):
    '''
        Prints every .PNG image inside of a folder 
    '''
    [print(x.name) for x in dir.iterdir() if x.suffix == '.png']

def print_all_jpg(dir):
    '''
        Prints every .JPG image inside of a folder 
    '''
    [print(x.name) for x in dir.iterdir() if x.suffix == '.jpg']
    
