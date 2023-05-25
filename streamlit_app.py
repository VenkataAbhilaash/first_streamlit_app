import streamlit
import pandas
import requests
import snowflake.connector
streamlit.title("My parents new healthy diner!")
streamlit.header("Breakfast Favourites")
streamlit.text("🥣 Omega 3 and Bluberry Oatmeal")
streamlit.text("🥗 Kale,Spinach and Rocket Smoothie")
streamlit.text("🐔 🍞 Hard-Boiled Free-Range Eggs")
streamlit.text("🥑 Avacado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list=my_fruits_list.set_index('Fruit')
my_fruits_selection=streamlit.multiselect("Pick some fruits:",list(my_fruits_list.index),['Avocado','Strawberries'])
my_fruits_show=my_fruits_list.loc[my_fruits_selection]
streamlit.dataframe(my_fruits_show)
streamlit.header("FruityVice's first Advice!")
streamlit.text("Which fruit data you want to look at ?")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Mango')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response= requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit details are :")
streamlit.dataframe(my_data_row)
