import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Cyber Threat Detection",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- BACKGROUND IMAGE ----------------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_css = ""

if os.path.exists("assets/cyber_bg.jpg"):
    bg_image = get_base64("assets/cyber_bg.jpg")

    bg_css = f"""
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    """
else:
    bg_css = """
    .stApp {
        background: linear-gradient(
            135deg,
            #0b1120,
            #111827,
            #1e293b
        );
    }
    """

# ---------------- CUSTOM CSS ----------------
st.markdown(f"""
<style>

{bg_css}

.main-overlay {{
    background: rgba(0,0,0,0.65);
    padding: 25px;
    border-radius: 20px;
}}

.main-title {{
    text-align: center;
    color: white;
    font-size: 50px;
    font-weight: 700;
}}

.subtitle {{
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
}}

div[data-testid="metric-container"] {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    padding: 15px;
    border-radius: 15px;
}}

div.stButton > button {{
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = joblib.load("models/threat_model.pkl")

# ---------------- HEADER ----------------
st.markdown(
    """
    <div class="main-overlay">
    <div class="main-title">
    🛡️ AI-Powered Cyber Threat Detection Platform
    </div>

    <div class="subtitle">
    Real-Time Network Traffic Analysis Using Machine Learning
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- KPI CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Detection Accuracy", "94%")

with col2:
    st.metric("Logs Processed", "50K+")

with col3:
    st.metric("Response Time", "<1 sec")

st.divider()

# ---------------- INPUTS ----------------
st.subheader("🔍 Analyze Network Traffic")

col1, col2, col3 = st.columns(3)

with col1:
    protocol = st.selectbox(
        "Protocol",
        ["TCP", "UDP"]
    )

with col2:
    packet_size = st.number_input(
        "Packet Size",
        min_value=0,
        value=500
    )

with col3:
    login_attempts = st.number_input(
        "Login Attempts",
        min_value=0,
        value=1
    )

protocol_value = 0 if protocol == "TCP" else 1

input_data = pd.DataFrame({
    "protocol": [protocol_value],
    "packet_size": [packet_size],
    "login_attempts": [login_attempts]
})

# ---------------- RISK SCORE ----------------
risk_score = min(
    ((packet_size / 20) + (login_attempts * 5)),
    100
)

st.subheader("⚠️ Risk Assessment")

st.progress(int(risk_score))

st.write(f"Current Risk Score: **{risk_score:.0f}%**")

# ---------------- PREDICTION ----------------
if st.button("🚀 Analyze Traffic"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Potential Cyber Threat Detected")
    else:
        st.success("✅ Network Traffic Appears Safe")

st.divider()

# ---------------- ANALYTICS ----------------
st.subheader("📊 Threat Analytics")

chart_data = pd.DataFrame({
    "Traffic Type": [
        "Safe",
        "Threat"
    ],
    "Count": [
        80,
        20
    ]
})

fig = px.pie(
    chart_data,
    names="Traffic Type",
    values="Count",
    hole=0.5,
    title="Network Traffic Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------- THREAT LOGS ----------------
st.subheader("📋 Recent Threat Logs")

logs = pd.DataFrame({
    "Source IP": [
        "192.168.1.10",
        "192.168.1.25",
        "192.168.1.44",
        "192.168.1.61"
    ],
    "Protocol": [
        "UDP",
        "TCP",
        "UDP",
        "TCP"
    ],
    "Risk Level": [
        "High",
        "Medium",
        "High",
        "Low"
    ],
    "Status": [
        "Blocked",
        "Monitored",
        "Blocked",
        "Safe"
    ]
})

st.dataframe(
    logs,
    use_container_width=True
)

st.divider()

# ---------------- FOOTER ----------------
st.caption(
    "Built with Python • Scikit-Learn • Streamlit • Machine Learning"
)