import streamlit as st
import datetime
import requests
import pandas as pd
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time'''
date_time = st.date_input("Sélectionnez la date", datetime.date.today())
time = st.time_input("Sélectionnez l'heure", datetime.datetime.now().time())
pickup_datetime= datetime.datetime.combine(date_time, time)
'''
- pickup longitude

'''

pickup_longitude = st.number_input("Longitude de départ", value=-73.950655)



'''
- pickup latitude

'''
pickup_latitude = st.number_input("Latitude de départ", value=40.783282)


'''
- dropoff longitude
'''
dropoff_longitude=st.number_input('Longitude de dropoff',value=-73)
'''

- dropoff latitude
'''
dropoff_latitude = st.number_input("Latitude de dropoff", value=40)
'''
- passenger count
'''
passenger_count = st.slider("Nombre de passagers", 1, 8, 1)
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
dic = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}



if st.button("Connect API"):
    st.write(requests.get(url, params=dic))

if st.button("Prediction"):
    st.write(f"The prediction is {requests.get(url, params=dic).json()['fare']}")
