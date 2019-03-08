import numpy as np
from PIL import Image
from flask import current_app as app
from pytesseract import image_to_string

import os
from flask import (
        Flask, Blueprint, render_template, request
)
from werkzeug.utils import secure_filename

bp = Blueprint('label', __name__, url_prefix='/label')



@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/uploader', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:
            #config the folder for upload image and rename it
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],"img.png"))

            img = Image.open('ingredients-label/static/img/img.png')

            img = img.convert('L')

            text = image_to_string(img)

            countRotate = 0

            while (text.find("INGREDIENTS") == -1 or text == ""):
                #print("inside while loop")

                # convert to grayspace
                img = img.convert('L')

                # rotate it
                img = img.rotate(90)
                #save = img.save('saveimg.jpg')
                text = image_to_string(img)

                countRotate = countRotate + 1
                print("count ", countRotate)
                if(countRotate >3):
                    text ="Not Found."
                    break

            # getting text into a list of words
            if(text.find("INGREDIENTS")!=-1):
                indexOfIn = text.find("INGREDIENTS")
                index = indexOfIn + 12
                startIndex = index
                while(text[index]!="."):
                    index = index +1

                dictlist = text[startIndex: index]
                dictlist = dictlist.strip()
                words = dictlist.split(",")


                for word in words:
                    print word
            
            return text
    return "no file"
