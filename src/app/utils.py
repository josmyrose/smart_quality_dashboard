
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

def preprocess_sensor_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def train_model(sensor_df, defect_df):
    # Simple feature: higher temp + vibration -> more defects
    df = sensor_df.copy()
    df['defect'] = (df['temperature'] > 80) | (df['vibration'] > 0.06)
    df['defect'] = df['defect'].astype(int)
    
    X = df[['temperature', 'vibration', 'pressure', 'speed']]
    y = df['defect']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    
    joblib.dump(clf, 'model.pkl')

def predict_defect(model, input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict_proba(input_df)[0][1]  # Probability of defect
    return prediction
