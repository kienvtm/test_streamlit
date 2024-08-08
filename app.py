import streamlit as st
import pandas as pd

# Sample data
data = {
    'user_id': ['user1', 'user2', 'user1', 'user3'],
    'value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# User authentication (simple version for demonstration)
def authenticate(username, password):
    user_data = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3'
    }
    if username in user_data and user_data[username] == password:
        return True
    return False

# Streamlit UI
st.title('Streamlit App with Row-Level Security')

username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button('Login'):
    if authenticate(username, password):
        st.success(f'Welcome, {username}!')
        # Filter data based on the authenticated user
        user_data = df[df['user_id'] == username]
        st.write('Your Data:')
        st.write(user_data)
    else:
        st.error('Invalid username or password')

