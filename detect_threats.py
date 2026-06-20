import joblib
import pandas as pd

model = joblib.load("models/threat_model.pkl")

sample = pd.DataFrame({
    "protocol": [1],
    "packet_size": [1500],
    "login_attempts": [10]
})

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Threat Detected")
else:
    print("Safe Traffic")