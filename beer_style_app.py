import streamlit as st
import joblib
import pandas as pd

# Load the KNN model
model = joblib.load('models/knn-k3.joblib')

# Load brewery names
with open('models/brewery_names.pkl', 'rb') as file:
    brewery_names = pd.read_pickle(file)

print(brewery_names)

# Create input fields for new data points
st.write("Enter new data points:")
brewery_name = st.selectbox('Brewery Name', brewery_names)
review_aroma = st.slider('Review Aroma (1-5)', min_value=1.0, max_value=5.0, step=0.1)
review_appearance = st.slider('Review Appearance (1-5)', min_value=1.0, max_value=5.0, step=0.1)
review_palate = st.slider('Review Palate (1-5)', min_value=1.0, max_value=5.0, step=0.1)
review_taste = st.slider('Review Taste (1-5)', min_value=1.0, max_value=5.0, step=0.1)
beer_abv = st.slider('Beer ABV', min_value=0.0, max_value=95.0, step=0.1)

# Create a button to predict beer style
if st.button('Predict Beer Style'):
    # Prepare the data for prediction
    new_data = {
        'brewery_name': brewery_name,
        'review_aroma': review_aroma,
        'review_appearance': review_appearance,
        'review_palate': review_palate,
        'review_taste': review_taste,
        'beer_abv': beer_abv
    }

    # Create a DataFrame from the new data
    new_data_df = pd.DataFrame([new_data])

    # Make a prediction using the pre-trained KNN model
    prediction = model.predict(new_data_df)

    # Display the predicted beer style
    st.write(f'<h2>Predicted Beer Style: {prediction[0]}</h2>', unsafe_allow_html=True)
