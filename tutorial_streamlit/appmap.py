import streamlit as st
import pandas as pd
import altair as alt


#make a title for this demo using emojis
st.title('DataFrame Demo')

## Elements on the sidebar
#st.sidebar.selectbox('Choose a demo', ['DataFrame Demo', 'Other'])
#check=st.sidebar.checkbox('Show code')

#write some text describing the app
'''
This is a demo shows how to use `st.write` to visualize Pandas DataFrames

[Data courtesy of the [UN Data Explorer](http://data.un.org/Data.aspx?d=FAO&f=itemCode%3a2051).)
'''
df = pd.read_csv('data1.csv')

# make a list with the countries in the dataframe
countries = df['Country or Area'].unique()
#st.write(countries)

##make a multiselect box with the countries
country_select = st.multiselect('Choose Countries', countries, default=['Chile','Mexico'])
#st.write(country_select)