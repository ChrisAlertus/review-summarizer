import numpy as np 
import pandas as pd 
import requests 
import streamlit as st 
  
# defining the api-endpoint  
API_ENDPOINT = '<mlhost>'

st.title('AISC NLP and ML Ops workshop March 2020')
st.write('While the rest of the world is holed up fleeing the spread of the'
    'COVID-19 coronavirus, a team of brave engineers was coding away on a Zoom'
    ' call.')

@st.cache(allow_output_mutation=True)
def get_state():
  return []

reviews = get_state()

st.write('Below, you can enter a review for your last meal ' 
    'and our model will summarize your review! Click the button once you '
    'finish typing your review')
review = st.text_input(label='your review here', value='')

if st.button('Add review'):

  #r = requests.post(url = API_ENDPOINT, data = review) 
  reviews.append((review, 'other'))

  formatted_reviews = ''
  for rev, summ in reviews:
    formatted_reviews = f'\nManual review said: {rev:>40}'
    formatted_reviews += f'\n\nSummary (ML generated) said: {summ:>40}\n'
    st.write(formatted_reviews)


# review_id = 0
# reviews = []
# review = None

# default = ''

#   # review added to data frame : clear the review box when button clicked
#   # send post request
#   # disiplay summary
# #if st.button('Add a review', key='write'):
# if st.button('reset box', key='reset'):
#   review = st.text_input(label='your review here', value=default,
#     key=review_id)
#   reviews.append(review)
#   print(review)
#   reviews.append(review)
#   default = ' '