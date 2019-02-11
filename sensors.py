
from flask import (
    Blueprint, jsonify, request)

from database import get_db, query_as_json

bp = Blueprint('sensors', __name__, url_prefix='/sensors')


@bp.route('/get_all', methods=['GET'])
def get_all():
    sensors = query_as_json('SELECT * FROM sensor')
    print sensors
    return jsonify(sensors)


@bp.route('/new_sensor', methods=['POST'])
def new_sensor():
    db = get_db()
    code = request.form["code"]
    name = request.form["name"]
    path = request.form["path"]
    type = request.form["type"]
    if code and name and path and type:
        db.execute('INSERT INTO sensor (code, name, path, type) VALUES (?,?,?,?)',(code,name,path,type))
        db.commit()
    return jsonify({"status": "OK"})



