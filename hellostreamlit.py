import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.image("http://www.weetablet.com/wp-content/uploads/2016/03/logo_small.png", width=100)
st.title('My first app')
st.header('This is a basic header')

st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

st.header('Random numbers')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

if st.checkbox('Show chart data'):
	chart_data
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
if st.checkbox('Show Map'):
	st.map(map_data)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

st.write('You selected: ', option)

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

