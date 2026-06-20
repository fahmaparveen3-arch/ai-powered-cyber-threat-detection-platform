import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("network_logs.csv")

df["protocol"] = df["protocol"].map({
    "TCP":0,
    "UDP":1
})

X = df[["protocol","packet_size","login_attempts"]]
y = df["threat"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = RandomForestClassifier()

model.fit(X_train,y_train)

joblib.dump(
    model,
    "models/threat_model.pkl"
)

print("Model Trained Successfully")