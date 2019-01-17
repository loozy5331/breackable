from PIL import Image
import os


def convert_to_jpg():
    for file in os.listdir("../original_images/"):
        if(file.split(".")[-1] != "jpg"):
            try:
                image = Image.open(file)
                image.convert("RGB")
                image.save(file.split(".")[0] + ".jpg")
            except:
                print(file + "can't change jpg file")
                pass
    print("finished convert!")
    return None


