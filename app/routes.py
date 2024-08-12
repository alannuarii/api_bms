from app import app
from flask import jsonify


@app.route('/test')
def testing():
    response = {"message":"Cuma test"}
    return jsonify(response), 200