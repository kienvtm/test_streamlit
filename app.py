import streamlit as st
import pandas as pd
import numpy as np

# # Sample data
# data = {
#     'user_id': ['user1', 'user2', 'user1', 'user3'],
#     'value': [10, 20, 30, 40]
# }
# df = pd.DataFrame(data)

# # User authentication (simple version for demonstration)
# def authenticate(username, password):
#     user_data = {
#         'user1': 'password1',
#         'user2': 'password2',
#         'user3': 'password3'
#     }
#     if username in user_data and user_data[username] == password:
#         return True
#     return False

# # Streamlit UI
# st.title('Streamlit App with Row-Level Security')

# username = st.text_input('Username')
# password = st.text_input('Password', type='password')

# if st.button('Login'):
#     if authenticate(username, password):
#         st.success(f'Welcome, {username}!')
#         # Filter data based on the authenticated user
#         user_data = df[df['user_id'] == username]
#         st.write('Your Data:')
#         st.write(user_data)
#     else:
#         st.error('Invalid username or password')



"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)