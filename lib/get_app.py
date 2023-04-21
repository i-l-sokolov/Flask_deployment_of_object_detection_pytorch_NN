import os
from lib.processing import object_detection_api
from flask import Flask, render_template, request

os.environ['WERKZEUG_RUN_MAIN'] = 'true'


def getting_app():

    app = Flask(__name__,static_folder='../static',template_folder='../templates')
    app.config["PATH_TO_UPLOAD"] = os.path.join("static", "img")

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/home')


    @app.route('/upload', methods=["GET", "POST"])
    def upload():
        if request.method == "GET":
            return render_template("upload.html")
        elif request.method == 'POST' and 'photo' in request.files:
            image = request.files['photo']
            PATH = os.path.join(app.config["PATH_TO_UPLOAD"], image.filename)
            image.save(PATH)
            image = object_detection_api(PATH, threshold=0.8)
            files = os.listdir(app.config["PATH_TO_UPLOAD"])
            i = len(files)
            path_to_res = os.path.join(app.config["PATH_TO_UPLOAD"], "image" + str(i) + ".jpg")
            image.save(path_to_res)
            return render_template("result.html", PATH_TO_SOURCE=PATH, PATH_TO_RESULTS=path_to_res)

    return app
