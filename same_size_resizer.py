from PIL import Image
import os
import sys
from pathlib import Path


##Put this script in the same directory of the images

if len(sys.argv) <= 3:
    print ('usage: same_size_resizer.py [Wigth of image] [Higth of the image] [Output Folder] ...eg: same_size_resizer.py 300 300 newFolder')
    sys.exit(1)

size = (int(sys.argv[1]),int(sys.argv[2]))
folderName = sys.argv[3]
extention = 'jpg'
path_here = Path('./'+folderName)
path_forLoop = ('./')

if path_here.is_dir():
    print('Folder exists!')
else:
    print('Folder Created!')
    os.mkdir('./' + str(folderName))

for file in os.listdir(path_forLoop):
    if file.endswith('.'+ str(extention)):
        i = Image.open(file)
        fn, fext = os.path.splitext(file)
        i.thumbnail(size)
        i.save('./'+folderName+'/{}_new{}'.format(fn, fext))
  
print("This will not crop image")        
print("This program sacaled the image in order to stay with the ratio of the original image.")

        
        