import json
import os.path

from flask import Flask, request
import tesserocr
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/png_to_text', methods=["POST"])
def png_to_text():
    png = request.files.get("png")
    lang = request.form.get('lang', "redops")
    image = Image.open(png.stream)
    text = tesserocr.image_to_text(image, lang=lang, path="./traineddata")
    return json.dumps({"text": text.strip()})


@app.route('/traineddata', methods=["POST"])
def trained_data():
    f = request.files.get("file")
    path = os.path.join("./traineddata", secure_filename(f.filename))
    f.save(path)
    return json.dumps({"msg": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
