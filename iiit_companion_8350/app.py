import streamlit as st
from microservices import *

st.title('IIIT Companion')

st.header('ResourceAvailabilityService')
ResourceAvailabilityService().run()

st.header('PersonalDashboardService')
PersonalDashboardService().run()
