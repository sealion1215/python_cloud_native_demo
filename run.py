from app import application, db
from app.blueprint.ocrreader.views import ocr_reader
from app.blueprint.ocrreader.models import RecognitionResult
from config import ddl, port_number
from constants import DDLMode
from flask_cors import CORS

application.register_blueprint(ocr_reader, url_prefix='/ocrreaders')

if ddl is DDLMode.CREATE:
    db.create_all()
    db.session.commit()
elif ddl is DDLMode.CREATE_DROP:
    db.drop_all()
    db.create_all()
    db.session.commit()

CORS(application)
application.run(host='0.0.0.0', port=port_number)
