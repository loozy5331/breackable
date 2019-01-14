import os

import xml.etree.ElementTree as ET
from PIL import Image, ImageFilter

class ImageImage:

    def __init__(self, file_path, kind_num=1):
        # 최대 5개까지 가능
        self.file_path = file_path
        self.kind_num = kind_num
        self.FILTERS = ["BOXBLUR", "UNSHARPMASK", "KERNEL", "MINFILTER", "MODEFILTER"]

    # 경로 안의 모든 이미지들을 읽어서 리스트 반환
    def load_images(self):
        image_list = list()
        for file in os.listdir(self.file_path):
            extension = file.split(".")[-1]
            if(extension != "xml"):
                image_list.append("../" + self.file_path + file)
        return image_list

    # 경로 안의 모든 xml 파일들을 읽어서 리스트 반환
    def load_xmls(self):
        xml_list = list()
        for file in os.listdir(self.file_path):
            extension = file.split(".")[-1]
            if (extension == "xml"):
                xml_list.append("../" + self.file_path + file)
        return xml_list

    # kind_num 만큼 Filter를 통해 이미지의 수를 늘려줌.
    def convert_images(self):
        image_path_list = self.load_images()
        for image_path in image_path_list:
            image_name = image_path.split(".")[0]
            image = Image.open(image_path)
            image.convert("RGB")
            image.save()

    # Filter 함수. 폴더를 만들고 그 안에 filter된 이미지를 이름을 조금 바꿔서 저장
    def make_BoxBlur(self):
        image_path_list = self.load_images()
        pass

    def make_UnsharpMask(self, image, image_name):
        if not "make_UnsharpMask_images" in os.listdir("../"):
            os.mkdir("../make_UnsharpMask_images")
        image.filter(ImageFilter.UnsharpMask(2))
        image.save(image_name + "_usm" + ".jpg")


    def make_Kernel(self, image, image_name):
        if not "make_Kernel_images" in os.listdir("../"):
            os.mkdir("../make_Kernel_images")
        image.filter(ImageFilter.Kernel((3, 3), [0.1*i for i in range(9)]))
        image.save(image_name + "_kn" + ".jpg")


    def make_MinFilter(self, image, image_name):
        if not "make_MinFilter_images" in os.listdir("../"):
            os.mkdir("../make_MinFilter_images")
        image.filter(ImageFilter.MinFilter())
        image.save(image_name + "_mf" + ".jpg")


    def make_ModeFilter(self, image, image_name):
        if not "make_ModeFilter_images" in os.listdir("../"):
            os.mkdir("../make_ModeFilter_images")
        image.filter(ImageFilter.ModeFilter(2))
        image.save(image_name + "_md" + ".jpg")



    # original xml 파일들을 통해 kind_num만큼
    # filename과 path를 바꿔서 xml를 늘려줌.
    def change_xml_files(self, xml_list):
        pass
