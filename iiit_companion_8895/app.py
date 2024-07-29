import streamlit as st
from microservices import *

st.title('IIIT Companion')

st.header('NotificationService')
NotificationService().run()

st.header('UserLocationService')
UserLocationService().run()
