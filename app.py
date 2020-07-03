from flask import Flask, render_template, url_for, request
import os
from PIL import Image
from processing import *


app = Flask(__name__)
app.config["PATH_TO_UPLOAD"] = os.path.join("static", "img")

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == 'POST' and 'photo' in request.files:
        image = request.files['photo']
        PATH = os.path.join(app.config["PATH_TO_UPLOAD"], image.filename)
        image.save(PATH)
        print("this is PATH", PATH)
        image = object_detection_api(PATH, threshold=0.8)
        print("this is after detection")
        files = os.listdir(app.config["PATH_TO_UPLOAD"])
        i = len(files)
        path_to_res = os.path.join(app.config["PATH_TO_UPLOAD"], "image"+str(i)+".jpg")
        print("this is path to res", path_to_res)
        image.save(path_to_res)
        print("this is print after save")
        #print(dir(image))
        #print("Next will be image")
        #print("this is type of upload image", type(image))
        #print("this is upload image", image)
        #print(image.filename)
        return render_template("result.html", PATH_TO_SOURCE = PATH, PATH_TO_RESULTS = path_to_res)

if __name__ == "__main__":
    app.run(debug=True)
