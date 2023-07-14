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


def get_fruitvice_data(this_fruit_choice):
    frt_response = requests.get("https://fruityvice.com/api/fruit/" + frt_choice)  
    frt_normlized = pandas.json_normalize(frt_response.json())
    return frt_normlized
def get_fruit_load_list():
    my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    my_data_row=my_cur.fetchall()
    my_cnx.close()
    return my_data_row

def insert_row_snowflake(new_fruit):
    try:       
        with my_cnx.cursor() as my_cur:
            #my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
            my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('" + ???? + "')")
            return "Thnx fr adding me " + new_fruit
    except Exception as e:
        streamlit.text(e)

streamlit.header("Fruit Advice...")
try:
    frt_choice = streamlit.text_input("what fruit info you would to have "," kiwi")
    if not frt_choice:
        streamlit.error("Pls select fruit to get info...")
    else:
        streamlit.write("the user entered fruit choice is is ",frt_choice)
        fun_response = get_fruitvice_data(frt_choice)
        streamlit.dataframe(fun_response)
except URLError as e:
    streamlit.error()


streamlit.text("The fruit load list Contains......")
if streamlit.button("Get Fruit Load List"):
    my_data_row_fun=get_fruit_load_list()
    streamlit.dataframe(my_data_row_fun)

add_fruit = streamlit.text_input("add new fruit ")
if streamlit.button("Add fruit to the list"):
    my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
    bck_frm_fun = insert_row_snowflake(add_fruit)
    my_cnx.close()
    streamlit.text(bck_frm_fun)
