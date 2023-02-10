'''
Image converter (mostly PNG to JPG)
1) Get directory
2) Create default folder
3) Convert all PNG to JPG in directory (create new file)
4) Send converted (new files) to default folder
5) yay, it works?

'''

from pathlib import Path
from PIL import Image
from utilities import directories  
            
def convert(dir, new_dir, dir_list):
    ''' converts file to JPG '''
    for x in dir.iterdir():
        if x.suffix == '.png':
            output = Path(dir.as_posix() + '\\' + x.stem + '.jpg')
            if directories.check_img_in_dir(output, new_dir, dir_list): continue
            if output != x:
                try:
                    with Image.open(x) as im:
                        im.save(output.name)
                        # im.show()
                        print(f"converted {x.name} to JPEG.")
                        directories.move_img_to_folder(output, new_dir)
                except OSError:
                    print('Cannot convert', x.name, '\n')          
                
def main():        
    ''' main function '''
    while True:
        dir = directories.input_dir()
        directories.change_dir(dir)
        directories.print_cwd()
        new_dir = directories.create_dir(dir)
        dir_list = directories.create_dir_list(new_dir)
        convert(dir, new_dir, dir_list)

main()
