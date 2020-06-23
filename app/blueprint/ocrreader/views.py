from app.blueprint.ocrreader.services import recognize_english_from_image
import base64
from config import log_level
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
import io
import logging
from PIL import Image
import sys

ocr_reader = Blueprint('ocr reader', __name__)
logger = logging.getLogger(__name__)
logger.setLevel(log_level)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


@cross_origin()
@ocr_reader.route('/english', methods=['POST'])
def recognize_english():
    logger.info('recognize_english')
    data = request.json
    return_dict = {}
    if data is not None:
        image_string = data['image']

        if data['isBase64String']:
            comma_index = image_string.find(',')
            if comma_index >= 0:
                image_string = image_string[comma_index+1:]
            logger.debug((image_string + '===')[:10])
            image_string = base64.b64decode(image_string+'===')

        bytes_io = io.BytesIO(image_string)
        bytes_io.seek(0)
        image = Image.open(bytes_io)
        result = recognize_english_from_image(image)
        return_dict['result'] = result
    else:
        logger.warning('invalid request body')
    return jsonify(return_dict)
