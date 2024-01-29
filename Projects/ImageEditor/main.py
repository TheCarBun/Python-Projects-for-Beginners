from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = './editedImages'

for filename in os.listdir(path):
    if filename.endswith("png") or filename.endswith("jpg"):
        try:
            img = Image.open(f"{path}/{filename}")
            edit = img.filter(ImageFilter.SMOOTH).convert("L")

        # Convert to RGB mode if necessary
            if edit.mode == 'RGBA':
                edit = edit.convert('RGB')

            clean_name = os.path.splitext(filename)[0]

            edit.save(f'{pathOut}/{clean_name}_edited.jpg')
        except:
            print(f"Error editing file {filename}")
        else:
            print(f"{filename} successfully edited")