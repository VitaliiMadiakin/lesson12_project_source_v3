from flask import Flask, request, render_template, send_from_directory
from functions import find_post, post_upload
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging

logger_info = logging.getLogger()
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("info.txt", 'w', 'utf-8')
logger_info.addHandler(console_handler)
logger_info.addHandler(file_handler)

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/list")
def page_tag():
    pass


@app.route('/post_by_tag.html')
def search():
    s = request.args.get("s").lower()
    posts = find_post(s)
    logger_info.warning(f"Выполнен поиск по - {s}")
    return render_template('post_list.html', s=s, posts=posts)


@app.route("/post", methods=["GET"])
def page_post_form():
    return render_template('post_form.html')


@app.route("/post_uploaded.html", methods=["POST"])
def page_post_upload():

    picture = request.files.get("picture")
    content = request.form.get("content")
    filename = picture.filename
    result = post_upload(picture, content, filename)
    if not result:
        return render_template('post_uploaded.html', content=content, filename=filename)
    else:
        return result


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
