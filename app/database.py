


# 📄 `app/database.py`

import pandas as pd

def load_data():
    sensor_data = pd.read_csv('../data/sensor_logs.csv')
    defect_data = pd.read_csv('../data/defect_reports.csv')
    return sensor_data, defect_data
def load_maintenance_data():
    return pd.read_csv('../data/maintenance_logs.csv')
