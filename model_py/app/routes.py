from flask import Blueprint, request, make_response, jsonify
from app.controllers import perform_prediction

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/predict')
def predict_op():
    try:
        date = request.args.get('date')
        pre1, pre2, pre3, pre4 = perform_prediction(date)

        return make_response(jsonify(str(pre1), str(pre2), str(pre3), str(pre4)))
    except Exception as e:
        return make_response(jsonify('Model service is down from model \n'), 404)
