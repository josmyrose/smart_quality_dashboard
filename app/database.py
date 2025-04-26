


# 📄 `app/database.py`

import pandas as pd

def load_sensor_data():
    return pd.read_csv('../data/sensor_logs.csv')

def load_defect_data():
    return pd.read_csv('../data/defect_reports.csv')

def load_maintenance_data():
    return pd.read_csv('../data/maintenance_logs.csv')
