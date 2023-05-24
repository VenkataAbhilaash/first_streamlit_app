import streamlit
import pandas
streamlit.title("My parents new healthy diner!")
streamlit.header("Breakfast Favourites")
streamlit.text("🥣 Omega 3 and Bluberry Oatmeal")
streamlit.text("🥗 Kale,Spinach and Rocket Smoothie")
streamlit.text("🐔 🍞 Hard-Boiled Free-Range Eggs")
streamlit.text("🥑 Avacado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list=my_fruits_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:",list(my_fruits_list.index))
streamlit.dataframe(my_fruits_list)
