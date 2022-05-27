import streamlit as st
import datetime
import datetime
import requests
import pandas as pd



'''
# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
# Date
d = st.date_input(
    "Input date",
    datetime.date(2019, 7, 6))
st.write('The date is:', d)

# Time
t = st.time_input('Input time', datetime.time(8, 45))
st.write('The time is', t)

# Pickup longitude
pickup_longitude = st.number_input('Pickup longitude', value = 40.7614327)
st.write('The current number is ', pickup_longitude)

# Pickup latitude
pickup_latitude = st.number_input('Pickup latitude', value = -73.9798156)
st.write('The current number is ', pickup_latitude)

# dropoff longitude
dropoff_longitude = st.number_input('Dropoff longitude', value = 40.6513111)
st.write('The current number is ', dropoff_longitude)

# dropoff latitude
dropoff_latitude = st.number_input('Dropoff latitude', value = -73.8803331)
st.write('The current number is ', dropoff_latitude)

# passenger count
passenger_count = st.selectbox('How many passengers ?', [0,1,2,3,4,5], 2)

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# url = 'https://taxifare.lewagon.ai/predict'
url = 'https://ricky2-lcgaesopaq-ew.a.run.app/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

X_pred = {
    "key": "2013-07-06 17:18:00.000000119",
    "pickup_datetime": f'{d} {t}',
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
    }

response = requests.get(url, params=X_pred)

if st.button('Show fare'):
    print('Button clicked')
    print(response)
    # st.write(response.json())
    st.write(f'The fare will be: {round(response.json()["fare"],2)}$')


@st.cache
def get_map_data():

    return pd.DataFrame(
        [[pickup_longitude, pickup_latitude], [dropoff_longitude, dropoff_latitude]],
        columns=['lat', 'lon']
    )
df = get_map_data()

st.map(df)
