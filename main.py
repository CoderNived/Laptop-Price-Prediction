import streamlit as st
import numpy as np
import pickle
import re
import pandas as pd

# ===============================
# LOAD TRAINED MODEL & DATAFRAME
# ===============================
pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

# ===============================
# SAFE COLUMN DETECTION FUNCTION
# ===============================
def find_col(pattern):
    """Finds a column name in df matching a given pattern (case-insensitive)."""
    for col in df.columns:
        if re.search(pattern, col, re.IGNORECASE):
            return col
    st.error(f"❌ Could not find column matching '{pattern}' in dataframe!")
    st.stop()

# Dynamically find column names based on your actual df.pkl
company_col = find_col("company")
type_col = find_col("type")
cpu_col = find_col("cpu")
gpu_col = find_col("gpu")
os_col = find_col("os")
ram_col = find_col("ram")
hdd_col = find_col("hdd")
ssd_col = find_col("ssd")

# ===============================
# STREAMLIT PAGE SETUP
# ===============================
st.set_page_config(page_title="💻 Laptop Price Predictor", page_icon="💰", layout="centered")

st.title("💻 Laptop Price Predictor")
st.markdown("### Predict the price of a laptop based on its specifications 🔍")
st.write("---")

# ===============================
# USER INPUT SECTION
# ===============================
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('🏢 Brand', sorted(df[company_col].unique()))
    typename = st.selectbox('💼 Type', sorted(df[type_col].unique()))
    ram = st.select_slider('💾 RAM (GB)', options=sorted(df[ram_col].unique()))
    weight = st.number_input('⚖️ Weight (kg)', min_value=0.5, max_value=5.0, step=0.1)
    touchscreen = st.radio('🖐 Touchscreen', ['No', 'Yes'])
    ips = st.radio('🖥️ IPS Display', ['No', 'Yes'])

with col2:
    screen_size = st.number_input('📏 Screen Size (inches)', min_value=10.0, max_value=20.0, step=0.1)
    resolution = st.selectbox('🔹 Screen Resolution', 
        ['1920x1080','1366x768','1600x900','3840x2160','3200x1800',
         '2880x1800','2560x1600','2560x1440','2304x1440'])
    cpu = st.selectbox('⚙️ CPU', sorted(df[cpu_col].unique()))
    hdd = st.select_slider('🧠 HDD (GB)', options=sorted(df[hdd_col].unique()))
    ssd = st.select_slider('🚀 SSD (GB)', options=sorted(df[ssd_col].unique()))
    gpu = st.selectbox('🎮 GPU', sorted(df[gpu_col].unique()))
    os = st.selectbox('🪟 Operating System', sorted(df[os_col].unique()))

# ===============================
# PREDICTION LOGIC
# ===============================
if st.button('💰 Predict Price'):
    try:
        # Convert categorical to binary
        touchscreen = 1 if touchscreen == 'Yes' else 0
        ips = 1 if ips == 'Yes' else 0

        # Prevent invalid screen size
        if screen_size <= 0:
            st.warning("⚠️ Please enter a valid screen size.")
            st.stop()

        # Calculate PPI
        X_res, Y_res = map(int, resolution.split('x'))
        ppi = ((X_res**2 + Y_res**2)**0.5) / screen_size

        # ===============================
        # Dynamically match df.pkl column names
        # ===============================
        col_map = {
            company_col: company,
            type_col: typename,
            ram_col: ram,
            'Weight': weight,
            'Touchscreen': touchscreen,
            'Ips': ips,
            'ppi': ppi if 'ppi' in df.columns else ppi,  # auto-detect
            cpu_col: cpu,
            hdd_col: hdd,
            ssd_col: ssd,
            gpu_col: gpu,
            os_col: os
        }

        # Filter only columns that exist in df
        final_cols = [col for col in col_map if col in df.columns]
        final_values = [col_map[c] for c in final_cols]

        query = pd.DataFrame([final_values], columns=final_cols)

        # ===============================
        # Predict
        # ===============================
        predicted_price = int(np.exp(pipe.predict(query)[0]))

        # Display result
        st.success(f"💸 **Estimated Laptop Price: ₹{predicted_price:,}**")
        st.balloons()

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
