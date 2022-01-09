import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Price Predictor')


company = st.selectbox('Brand',df['Company'].unique())

type = st.selectbox('Type',df['TypeName'].unique())

ram = st.selectbox('RAM (in GB)',[2,4,8,12,16,24,32,64])

weight = st.number_input('Weight (in Kg)')

touchscreen = st.selectbox('Touchscreen',['No','Yes'])

Ips = st.selectbox('IPS',['No','Yes'])

screen_size = st.number_input('Screen Size',min_value=10)

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160',
'3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

cpu = st.selectbox('CPU',df['Cpu Brand'].unique())

hdd = st.selectbox('HDD (in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD (in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu Brand'].unique())

os = st.selectbox('OS',df['OS'].unique())

if st.button('Predict Price'):
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    
    if Ips == 'Yes':
        Ips = 1
    else:
        Ips = 0
    
    X_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = (((X_res**2) + (y_res**2))**0.5)/screen_size

    query = np.array([company,type,ram,weight,touchscreen,Ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The Price of Laptop is: Rs. "+str(int(np.exp(pipe.predict(query)[0]))))