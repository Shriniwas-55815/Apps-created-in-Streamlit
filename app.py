import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open(r'C:\Users\Shriniwas\Desktop\Program File\Non -Tech Project\practice simple linear regression model - Copy\linear_regression_model.pkl', 'rb'))


# Set the title of the Streamlit app
st.title("Salary Prediction App")

# Add a brief description
st.markdown("""
### Salary Prediction App

The **Salary Prediction App** is an interactive web application designed to estimate a person's monthly or annual salary based on their years of work experience.  
This application uses a pre-trained **Simple Linear Regression model** to make predictions, ensuring accuracy and reliability. """)


# Add input widget for user to enter years of experience
Yrs_Exp = st.number_input("Please Enter the Years of Work Experience ", min_value=0.0, max_value=50.0, value=1.0, step=0.5)

# When the button is clicked, make predictions
if st.button("Predict Salary"):
    # Make a prediction using the trained model
    Exp_input=np.array([[Yrs_Exp]])  # Convert the input to a 2D array for prediction
    Pred = model.predict(Exp_input)
    
    # Display the result
    st.success(f"The Predict Salary for {Yrs_Exp} Years of Experiences is : ₹{Pred[0]:,.2f}")


st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Display information about the model
st.markdown("""
#### Key Features:
- **User-friendly interface** powered by Streamlit.  
- **Input field** for specifying years of work experience, with a range of 0 to 50 years.  
- **Instant salary predictions** displayed with precision and clarity.  
- Built using a **dataset correlating salaries with years of experience**.  
- Developed by **Shriniwas Vijay Uttarkar** for practical use in career planning and financial forecasting.

This tool is ideal for professionals, recruiters, and career counselors who need a quick estimate of salary expectations based on work experience.


#### About the Model
This model was trained using a dataset mapping years of work experience to salary values.  
The predictions are based on a **Simple Linear Regression model** built by **Shriniwas Vijay Uttarkar**. """)