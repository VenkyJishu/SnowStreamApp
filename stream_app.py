import streamlit
<<<<<<< HEAD
streamlit.title('My Parents new healthy Dinner ??')
streamlit.header('Breakfast Menu')
=======
streamlit.title('My Parents new healthy Dinner')
streamlit.header('Breakfast Menu !!!')
>>>>>>> 52ce4419b53ac2be69b00e9c2fdc0973e101ea78
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg ???')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie ---> 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


<<<<<<< HEAD
streamlit.multiselect("Pick some fruits --> ",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
=======

fruits_selected = streamlit.multiselect("Pick some fruits ",list(my_fruit_list.index),['Avocado','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

>>>>>>> 52ce4419b53ac2be69b00e9c2fdc0973e101ea78
