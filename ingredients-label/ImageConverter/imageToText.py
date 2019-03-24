import numpy as np
from PIL import Image
from pytesseract import image_to_string


class Read():
    def __init__(self, filename, foodName):
        self.fileName = filename
        self.foodName = foodName

    def get_food(self):
        #foodName = input("Enter food name: ")
        self.foodName

    def get_fileName(self):
        #fileName = input("Enter file location: ")
        self.fileName

    def ocr(self):
        # convert to grayspace
        img = Image.open(self.fileName)
        img = img.convert('L')
        text = image_to_string(img)
        if (text.find('INGREDIENTS') != -1):
            isFound = 1
            print("Found")
        else:
            isFound = 0
            print("Not found")

        while (text.find("INGREDIENTS") == -1 or text == ""):
            print("inside while loop")

            # convert to grayspace
            img = img.convert('L')

            # rotate it
            img = img.rotate(90)
            save = img.save('saveimg.jpg')


            text = image_to_string(img)

        return text

class Store_Data(Read):
    def __init__(self, fileName, foodName):
        super().__init__(fileName, foodName)
        print(foodName)

    def dictionary_add(self):
        # split string into a list
        raw_text = Read.ocr(self)
        sep = raw_text.split(',')

        # create ingredients_dict variable
        ingredients_dict = dict.fromkeys(sep, self.foodName)

        # remove '\n' in ingredients_dict
        ingredients_dict = {key.strip(): item.strip() for key, item in ingredients_dict.items()}

        return ingredients_dict
