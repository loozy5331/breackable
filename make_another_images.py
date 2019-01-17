import os

import xml.etree.ElementTree as ET
from PIL import Image, ImageFilter

# 이미지를 불리는 용도의 클래스
# 요약: original 이미지에만 열심히 labeling을 하면 filter를 통해 5배의 이미지로 부풀려 준다!
class ImageImage:
    # 생성자로 원본이미지가 있는 파일, xml 파일에서 저장할 폴더 경로를 함께 매개변수로 입력해준다.
    def __init__(self, file_path, target_path, startNum):
        self.file_path = file_path
        self.target_path = target_path
        self.startNum = startNum

    # 경로 안의 모든 이미지들을 읽어서 이미지들의 경로 리스트 반환
    def load_images(self):
        image_list = list()
        for file in os.listdir(self.file_path):
            extension = file.split(".")[-1]
            if(extension != "xml"):
                image_list.append(self.file_path + file)
        return image_list

    # 경로 안의 모든 xml 파일들을 읽어서 xml 파일의 경로 리스트 반환
    def load_xmls(self):
        xml_list = list()
        for file in os.listdir(self.file_path):
            extension = file.split(".")[-1]
            if (extension == "xml"):
                xml_list.append(self.file_path + file)
        return xml_list

    # jpg 확장자로 변환해서 저장
    def convert_images(self):
        image_path_list = self.load_images()
        print("============Convert_image!==============")
        for cnt, image_path in enumerate(image_path_list):
            extention = image_path.split(".")[-1]
            image_name = str(cnt + self.startNum) + "-image"
            print(image_name)
            if extention == "jpg":
                continue
            image = Image.open(image_path)
            image = image.convert("RGB")    # 여기가 바꿔주는 부분.
            image.save("../original_images/" + image_name + ".jpg")
            os.remove(image_path)

    # 경로로 되어있는 것에서 이미지 이름만 뽑아준다.
    def extract_name(self, image_path):
        name = image_path[:-4].split("/")[-1]
        return name

    # 현재 xml 파일 경로, 파일명 뒤에 붙일 명칭, 저장할 위치의 폴더, xml 정보 내의 이미지 경로 정보
    def change_xml_info(self, xml_path, str_kind, directory, target_path):
        doc = ET.parse(xml_path)
        root = doc.getroot()
        filename_text = root.find('filename').text[:-4] + str_kind
        root.find('filename').text = filename_text + ".jpg"
        root.find('path').text = target_path + filename_text + ".jpg"
        #ET.dump(root) # xml 문서 확인용.
        ET.ElementTree(root).write("../{}/".format(directory) + filename_text + ".xml", encoding='utf-8')

    # =======================================================================================================
    # Filter 함수. 폴더를 만들고 그 안에 filter된 이미지를 이름을 조금 바꿔서 저장
    # BoxBlur : _bb
    # UnsharpMask : _usm
    # Kernel : _ker
    # MinFilter : _min
    # ModeFilter : _mode

    def make_BoxBlur(self):
        folderName = "make_BoxBlur_images"
        image_path_list = self.load_images()
        xml_path_list = self.load_xmls()
        print("============Make_BoxBlur!==============")
        if not folderName in os.listdir("../"):
            os.mkdir("../" + folderName)
        for image_path in image_path_list:
            print(self.extract_name(image_path))
            image = Image.open(image_path)
            image = image.filter(ImageFilter.BoxBlur(2))
            image.save("../{}/".format(folderName) + self.extract_name(image_path) + "_bb.jpg")
        for xml_path in xml_path_list:
            self.change_xml_info(xml_path, "_bb", folderName, self.target_path)


    def make_UnsharpMask(self):
        folderName = "make_UnsharpMask_images"
        image_path_list = self.load_images()
        xml_path_list = self.load_xmls()
        print("============Make_UncharpMask!==============")
        if not folderName in os.listdir("../"):
            os.mkdir("../" + folderName)
        for image_path in image_path_list:
            print(self.extract_name(image_path))
            image = Image.open(image_path)
            image = image.filter(ImageFilter.UnsharpMask(2))
            image.save("../{}/".format(folderName) + self.extract_name(image_path) + "_usm.jpg")
        for xml_path in xml_path_list:
            self.change_xml_info(xml_path, "_usm", folderName, self.target_path)


    def make_Kernel(self):
        folderName = "make_Kernel_images"
        image_path_list = self.load_images()
        xml_path_list = self.load_xmls()
        print("============Make_Kernel!==============")
        if not folderName in os.listdir("../"):
            os.mkdir("../" + folderName)
        for image_path in image_path_list:
            print(self.extract_name(image_path))
            image = Image.open(image_path)
            image = image.filter(ImageFilter.Kernel((3, 3), [0.0001*i for i in range(9)]))
            image.save("../{}/".format(folderName) + self.extract_name(image_path) + "_ker.jpg")
        for xml_path in xml_path_list:
            self.change_xml_info(xml_path, "_ker", folderName, self.target_path)


    def make_MinFilter(self):
        folderName = "make_MinFilter_images"
        image_path_list = self.load_images()
        xml_path_list = self.load_xmls()
        print("============Make_MinFilter!==============")
        if not folderName in os.listdir("../"):
            os.mkdir("../" + folderName)
        for image_path in image_path_list:
            print(self.extract_name(image_path))
            image = Image.open(image_path)
            image = image.filter(ImageFilter.MinFilter())
            image.save("../{}/".format(folderName) + self.extract_name(image_path) + "_min.jpg")
        for xml_path in xml_path_list:
            self.change_xml_info(xml_path, "_min", folderName, self.target_path)


    def make_ModeFilter(self):
        folderName = "make_ModeFilter_images"
        image_path_list = self.load_images()
        xml_path_list = self.load_xmls()
        print("============Make_ModeFilter!==============")
        if not folderName in os.listdir("../"):
            os.mkdir("../" + folderName)
        for image_path in image_path_list:
            print(self.extract_name(image_path))
            image = Image.open(image_path)
            image = image.filter(ImageFilter.ModeFilter(2))
            image.save("../{}/".format(folderName) + self.extract_name(image_path) + "_mode.jpg")
        for xml_path in xml_path_list:
            self.change_xml_info(xml_path, "_mode", folderName, self.target_path)


if __name__=="__main__":
    imageimage = ImageImage("../original_images/",
                            "/home/lee/바탕화면/models_body/research/object_detection/images/train/", 1)
    imageimage.convert_images()
    imageimage.make_BoxBlur()
    imageimage.make_UnsharpMask()
    imageimage.make_Kernel()
    imageimage.make_MinFilter()
    imageimage.make_ModeFilter()
