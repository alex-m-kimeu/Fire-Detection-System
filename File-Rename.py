# Convert image format
from PIL import Image
import os

path = 'path' # Replace with the path to your folder

for filename in os.listdir(path):
    if not filename.endswith('.png'): # Replace with the file extension of your images(png, jpg, jpeg, etc.)
        continue
        
    old_path = os.path.join(path, filename)
    new_path = os.path.join(path, os.path.splitext(filename)[0] + '.jpg')
    
    with Image.open(old_path) as im:
        im.convert('RGB').save(new_path)
    
    os.remove(old_path)

# Rename image name
import os

path = 'path' # Replace with the path to your folder
new_name = 'new_name' # Replace with the new name you want to use
extension = '.jpg' # Replace with the file extension of your images

i = 1

for filename in os.listdir(path):
    if filename.endswith(extension):
        old_path = os.path.join(path, filename)
        new_path = os.path.join(path, new_name + str(i) + extension)
        os.rename(old_path, new_path)
        i += 1
