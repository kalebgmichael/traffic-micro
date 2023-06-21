from flask import Flask, request, jsonify, redirect, url_for, session,make_response
from datetime import datetime
def data():
    file_path = "gate1.json"
    file = open(file_path, "r")
    file1 = request.form['file']
    gate_number = request.form.get('gate')
    try:
        if not file1.filename.endswith('.json'):
           return 'Invalid file type', 400

        file_content = file1.read().decode('utf-8')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    try:
        json_data = json.loads(file_content)
    except json.JSONDecodeError:
        return 'Invalid JSON content', 400

    for record in json_data:
        year = record['YEAR']
        month = record['MONTH']
        day = record['DAY']
        vehicle_count = record['VEHICLE_COUNT']