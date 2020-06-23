from app import db
from app.blueprint.ocrreader.models import RecognitionResult
from datetime import datetime
import pytesseract
from time import time


def recognize_english_from_image(image):
    result = pytesseract.image_to_string(image, lang='eng', config='--psm 10')
    result_record = RecognitionResult(id=int(round(time() * 1000)), language='english', result=result, date=datetime.now())
    db.session.add(result_record)
    db.session.commit()
    return result