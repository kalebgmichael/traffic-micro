import numpy as np
import pickle
import pandas as pd
from datetime import datetime

pickle_in1 = open("Gate1_Model.pkl", "rb")
pickle_in2 = open("Gate2_Model.pkl", "rb")
pickle_in3 = open("Gate3_Model.pkl", "rb")
pickle_in4 = open("Gate4_Model.pkl", "rb")

classifier1 = pickle.load(pickle_in1)
classifier2 = pickle.load(pickle_in2)
classifier3 = pickle.load(pickle_in3)
classifier4 = pickle.load(pickle_in4)

pickle_in1.close()
pickle_in2.close()
pickle_in3.close()
pickle_in4.close()

def predict_gate1(days):
    grouped_df1_size = 837
    pre1 = classifier1.predict(
        start=grouped_df1_size, end=grouped_df1_size+days, type='levels')
    return pre1.values[-1]

def predict_gate2(days):
    grouped_df2_size = 551
    pre2 = classifier2.predict(
        start=grouped_df2_size, end=grouped_df2_size+days, type='levels')
    return pre2.values[-1]

def predict_gate3(days):
    grouped_df3_size = 819
    pre3 = classifier3.predict(
        start=grouped_df3_size, end=grouped_df3_size+days, type='levels')
    return pre3.values[-1]

def predict_gate4(days):
    grouped_df4_size = 507
    pre4 = classifier4.predict(
        start=grouped_df4_size, end=grouped_df4_size+days, type='levels')
    return pre4.values[-1]

def perform_prediction(date):
    selected_date = datetime.strptime(date, '%Y-%m-%d')
    future_timestamp_new = pd.to_datetime(selected_date)
    current_timestamp1 = pd.to_datetime('2021-8-1')
    date_difference1 = future_timestamp_new - current_timestamp1
    days1 = date_difference1.days

    current_timestamp2 = pd.to_datetime('2021-7-30')
    date_difference2 = future_timestamp_new - current_timestamp2
    days2 = date_difference2.days

    current_timestamp3 = pd.to_datetime('2021-7-31')
    date_difference3 = future_timestamp_new - current_timestamp3
    days3 = date_difference3.days

    current_timestamp4 = pd.to_datetime('2021-7-31')
    date_difference4 = future_timestamp_new - current_timestamp4
    days4 = date_difference4.days

    pre1 = predict_gate1(days1)
    pre2 = predict_gate2(days2)
    pre3 = predict_gate3(days3)
    pre4 = predict_gate4(days4)

    return pre1, pre2, pre3, pre4
