import uuid

from flask import (
    Blueprint, jsonify, request)

import database
from database import get_db

bp = Blueprint('temperature', __name__, url_prefix='/temp')


@bp.route('/get_current')
def get_current():
    db = get_db()
    transaction = db.execute('SELECT trans FROM temp_record ORDER BY created DESC').fetchone()[0]
    if transaction:
        data = database.query_as_json('SELECT * FROM temp_record tr JOIN sensor s ON tr.sensor_id = s.id WHERE trans = ?', (transaction,))
        return jsonify(data)


@bp.route('/set_record', methods=['POST'])
def set_current():
    data = request.get_json()["data"]
    print data

    trans = uuid.uuid4().hex
    for sensor in data:
        sensor_id = database.query_as_json('SELECT id from sensor where code = ?', (sensor["code"],))[0]
        print sensor_id
        db = get_db()
        db.execute('INSERT INTO temp_record (sensor_id, value, trans) VALUES (?,?,?)',(sensor_id['id'],sensor["value"], trans))
        db.commit()

    return jsonify({"status": "OK"})