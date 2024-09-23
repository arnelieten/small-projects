import os
from PIL import Image

source_path = r'C:\Users\arnel\OneDrive\Python\Data\Images\images'
dest_path = r'C:\Users\arnel\OneDrive\Python\Data\Images\images_modified'


for images in os.listdir(source_path):
    img = Image.open(os.path.join(source_path,images))
    img = img.resize((128,128))
    img = img.rotate(-90)
    #insert other image operations
    img.save(os.path.join(dest_path, images))
    print(images)
