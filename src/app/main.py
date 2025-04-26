
from flask import Flask, request, jsonify
from model import load_model
from utils import predict_defect
from database import load_sensor_data, load_defect_data, load_maintenance_data
from utils import preprocess_sensor_data, train_model

app = Flask(__name__)

# Load and preprocess data
#sensor_data = preprocess_sensor_data(load_sensor_data())
#defect_data = load_defect_data()
try:
    sensor_data = preprocess_sensor_data(load_sensor_data())
    defect_data = load_defect_data()
except FileNotFoundError as e:
    print(f"Error loading sensor data: {e}")
    sensor_data = None
# Train model
train_model(sensor_data, defect_data)

# Load trained model
model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    input_json = request.json
    prediction = predict_defect(model, input_json)
    return jsonify({'defect_probability': prediction})

@app.route('/health', methods=['GET'])
def health():
    return "API is running!"

if __name__ == '__main__':
    app.run(debug=True)
