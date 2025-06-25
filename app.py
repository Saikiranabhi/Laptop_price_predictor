import streamlit as st
import joblib
import sklearn
import numpy as np 

st.title("Laptop Price Predictor")

pipe = joblib.load('pipe.jb')
df = joblib.load('data.jb')

# Brand
company = st.selectbox('Brand', df['Company'].unique())

# Type of laptop
laptop_type = st.selectbox('Type', df['TypeName'].unique())

# Ram
ram = st.selectbox('Ram(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# weight 
weight = st.number_input("Weight of the laptop")

# Touch_Screen 
touchscreen = st.selectbox('TouchScreen', ['No', 'Yes'])

# IPS 
ips = st.selectbox('IPS', ['No', 'Yes'])

# Screen_Size 
Screen_size = st.number_input('Screen size')

# Resolution
resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160', 
    '3200x1800','2880x1800', '2560x1600', '2560x1440', 
    '2304x1440'
])

# CPU
cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# Hardware
hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

# GPU
gpu = st.selectbox('GPU', df['Gpu brand'].unique())

# Type of OS
os = st.selectbox('Operating System', df['os'].unique())

if st.button('Predict Price'):
    # Encoding Touchscreen and IPS
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Calculating PPI
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((x_res**2) + (y_res**2))**0.5 / Screen_size

    # Query formation
    query = np.array([company, laptop_type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os], dtype=object)
    query = query.reshape(1, 12)

    # Predict and display
    pred = pipe.predict(query)[0]
    st.title("Predicted Price is " + str(int(np.exp(pred))))
