import streamlit

streamlit.title('My Parents new healthy Dinner ??')
streamlit.header('Breakfast Menu')

streamlit.title('My Parents new healthy Dinner')
streamlit.header('Breakfast Menu !!!')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg ???')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie ---> 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


streamlit.multiselect("Pick some fruits --> ",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


fruits_selected = streamlit.multiselect("Pick some fruits ",list(my_fruit_list.index),['Avocado','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruit Advice...")
streamlit.text_input("what fruit info you would to have "," kiwi")