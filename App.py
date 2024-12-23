import streamlit as st
import pickle as pkl
import numpy as np  # Add numpy import

# Load the pre-trained model
model_path = r'C:\Users\Shriniwas\A VS CODE\15. Machine Learning\Simple Linear Regression Model\Electric City Bill Project\Elec_LR_model.pkl'
model = pkl.load(open(model_path, 'rb'))

# Streamlit App Title
st.title("Electricity Bill Prediction App")

# Description of the app
st.write("""
This application is designed to help users estimate their monthly electricity bill based on various factors such as usage, appliance load, time of year (e.g., summer vs. winter), and more.
It uses a machine learning model to predict the bill amount based on historical data.
""")

# Input for kWh usage
kwh = st.number_input("Please Enter the Electricity Meter Usage (in kWh)", min_value=0.0, max_value=2500.0, value=200.0, step=50.0)

# Button to trigger prediction
if st.button("Predict Electricity Bill Amount"):
    # Convert the input to a 2D array for prediction
    Meter_input = np.array([[kwh]])
    
    # Make a prediction using the trained model
    Pred = model.predict(Meter_input)
    
    # Display the prediction result
    st.success(f"The Predicted Electricity Bill for {kwh} kWh usage is: ₹{Pred[0]:,.2f}")

# Adding space for aesthetics
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Optional: Display model information or other additional content
st.markdown("""
You can learn more about the model, how it was trained, and other relevant details here. App Build by Shriniwas Uttarkar
""")