import numpy as np 
import joblib
import streamlit as st 

obj = joblib.load('california.joblib')

model = obj['model']
cols = obj['columns']

st.title('california APP')

In = []

for i in cols:
    v = st.number_input(f'Enter {i} value :')
    In.append(v)

if st.button('click'):
    Input = np.array([In])
    out = model.predict([In])

    st.success(out)