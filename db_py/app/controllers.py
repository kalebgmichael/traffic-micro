from flask import request, jsonify
from app.models import VehicleRecord
from datetime import datetime
from app import app


def get_data():
    try:
        f = request.args.get('date')

        selected_date = datetime.strptime(f, '%Y-%m-%dT%H:%M')
        year = selected_date.year
        month = selected_date.month
        day = selected_date.day
        hour = selected_date.hour

        vehicle_records1 = VehicleRecord.query.filter_by(
            year=year, month=month, day=day, hour=hour, gate=1).all()
        vehicle_records2 = VehicleRecord.query.filter_by(
            year=year, month=month, day=day, hour=hour, gate=2).all()
        vehicle_records3 = VehicleRecord.query.filter_by(
            year=year, month=month, day=day, hour=hour, gate=3).all()
        vehicle_records4 = VehicleRecord.query.filter_by(
            year=year, month=month, day=day, hour=hour, gate=4).all()

        records1 = []
        records2 = []
        records3 = []
        records4 = []

        for record in vehicle_records1:
            records1.append({
                'id': record.id,
                'gate': record.gate,
                'year': record.year,
                'hour': record.hour,
                'day': record.day,
                'no_veh': record.no_veh
            })

        for record in vehicle_records2:
            records2.append({
                'id': record.id,
                'gate': record.gate,
                'year': record.year,
                'hour': record.hour,
                'day': record.day,
                'no_veh': record.no_veh
            })

        for record in vehicle_records3:
            records3.append({
                'id': record.id,
                'gate': record.gate,
                'year': record.year,
                'hour': record.hour,
                'day': record.day,
                'no_veh': record.no_veh
            })

        for record in vehicle_records4:
            records4.append({
                'id': record.id,
                'gate': record.gate,
                'year': record.year,
                'hour': record.hour,
                'day': record.day,
                'no_veh': record.no_veh
            })

        if not records1 and not records2 and not records3 and not records4:
            # No data found
            return jsonify({'error': 'No data found for the specified parameters'})

        return jsonify(records1, records2, records3, records4, f)

    except ValueError:
        # Handle invalid date format error
        return jsonify({'error': 'Invalid date format'}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500

