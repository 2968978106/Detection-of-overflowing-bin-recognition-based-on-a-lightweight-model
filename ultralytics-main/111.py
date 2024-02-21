import json
from flask_restful import reqparse, Resource, Api
from werkzeug.datastructures import FileStorage
from flask import Flask
from ultralytics import YOLO
import cv2

model = YOLO("best.pt")


def pred(im):
    results = model.predict(source=im, save=False, save_txt=False)

    cls = results[0].boxes.cls.numpy().tolist()
    conf = results[0].boxes.conf.numpy().tolist()
    xywh = results[0].boxes.xywh.numpy().tolist()

    r = {'r': []}
    names = results[0].names

    for i, j, k in zip(cls, conf, xywh):
        r['r'].append({'cls': names[i], 'conf': float(j), 'xywh': [float(kk) for kk in k]})

    return r


class UploadImg(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('imgFile', required=True, type=FileStorage, location='files', help="imgFile is wrong.")

    def post(self):
        img_file = self.parser.parse_args().get('imgFile')
        img_file.save(img_file.filename)
        rr = pred(img_file.filename)
        return json.dumps(rr), 201


if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(UploadImg, '/uploadimg')
    app.run()