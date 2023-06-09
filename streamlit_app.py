import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
    fruityvice_normalized= pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
streamlit.header("FruityVice's first Advice!")
try:
    streamlit.text("Which fruit data you want to look at ?")
    fruit_choice = streamlit.text_input('What fruit would you like information about?','Mango')
    if not fruit_choice:
          streamlit.error("Please select to get more information.")
    else:
        streamlit.write('The user entered ', fruit_choice)
        fruityvice_response= requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list as Fruits ")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains :")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("Select * from fruit_load_list")
        return my_cur.fetchall()
if streamlit.button("Get Fruit Load List"):
    my_cnx=snowflake.connector.connect(""streamlit.secrest["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    my_cnx.close()
streamlit.dataframe(my_data_row)
streamlit.text("Which fruit do you like to add ?")
fruit_input = streamlit.text_input('What fruit would you like to add ?','Jackfruit')
streamlit.write('Thanks for adding  ', fruit_input)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
streamlit.stop()
