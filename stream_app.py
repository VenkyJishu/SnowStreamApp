import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.title('My Parents new healthy Dinner ??')
streamlit.header('Breakfast Menu')

streamlit.title('My Parents new healthy Dinner')
streamlit.header('Breakfast Menu !!!')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg ???')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie ---> 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


streamlit.multiselect("Pick some fruits --> ",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


fruits_selected = streamlit.multiselect("Pick some fruits ",list(my_fruit_list.index),['Avocado','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)



streamlit.header("Fruit Advice...")
try:
    frt_choice = streamlit.text_input("what fruit info you would to have "," kiwi")
    if not frt_choice:
        streamlit.error("Pls select fruit to get info...")
    else:
        streamlit.write("the user entered fruit choice is is ",frt_choice)
        frt_response = requests.get("https://fruityvice.com/api/fruit/"+frt_choice)
        streamlit.text(frt_response)
        #api/fruit/banana
        frt_normlized = pandas.json_normalize(frt_response.json())
        streamlit.dataframe(frt_normlized)
except URLError as e:
    streamlit.error()

my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("select current_user(),current_account(),current_region()")
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_row=my_cur.fetchone()
my_data_row=my_cur.fetchall()
#streamlit.header("Hello from snowflake")
streamlit.header("fruit list contains")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

