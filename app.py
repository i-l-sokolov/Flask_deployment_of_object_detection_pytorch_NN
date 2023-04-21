from gevent.pywsgi import WSGIServer
import argparse
from lib.get_app import getting_app
from flask import Flask, render_template

# def index():
#     return render_template("index.html")


# @app.route('/upload', methods=["GET", "POST"])
# def upload():
#     if request.method == "GET":
#         return render_template("upload.html")
#     elif request.method == 'POST' and 'photo' in request.files:
#         image = request.files['photo']
#         PATH = os.path.join(app.config["PATH_TO_UPLOAD"], image.filename)
#         image.save(PATH)
#         image = object_detection_api(PATH, threshold=0.8)
#         files = os.listdir(app.config["PATH_TO_UPLOAD"])
#         i = len(files)
#         path_to_res = os.path.join(app.config["PATH_TO_UPLOAD"], "image"+str(i)+".jpg")
#         image.save(path_to_res)
#         return render_template("result.html", PATH_TO_SOURCE = PATH, PATH_TO_RESULTS = path_to_res)


# @app.route('/stop_server', methods=["GET"])
# def stop_server():
#     if request.method == "GET":
#         http_server.stop()
#         return "Server stopped"



# app = Flask(__name__)
# app.config["PATH_TO_UPLOAD"] = os.path.join("static", "img")


# @app.route('/')
# @app.route('/home')

parser = argparse.ArgumentParser(description='port number')
parser.add_argument('--port', type=int, default=8000, help='the port number of the http server')
args = parser.parse_args()
port = args.port





if __name__ == "__main__":
    # app.run(debug=True)

    app = getting_app()
    @app.route('/stop_server', methods=["GET"])
    def stop_server():
        render_template('server_stopped.html')
        http_server.stop()
        return render_template('server_stopped.html')

    http_server = WSGIServer(("127.0.0.1", port), app, log=None)
    print('Please follow the link to the object detection app:')
    print(f'http://127.0.0.1:{port}')
    http_server.serve_forever()
