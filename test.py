import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('My First Streamlit App')

# Add a slider widget
x = st.slider('Select a value', 0.0, 10.0, 5.0)

# Generate some example data
x_values = np.linspace(0, 10, 100)
y_values = np.sin(x_values * x)

# Plot the data
plt.plot(x_values, y_values)
st.pyplot(plt)
