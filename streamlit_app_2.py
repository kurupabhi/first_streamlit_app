import streamlit
import pandas
#import requests
#import snowflake.connector
#from urllib.error import URLError

streamlit.title('Breakfast')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## Add list of fruits
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
## Let's put a pick list here so they can pick the fruit they want to include 
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
## Display list
#streamlit.dataframe(fruits_to_show)
#
#
## Customer selected fruit.
#streamlit.text('Fruityvice Fruit Advice!')
#try:
#    fruit_choice = streamlit.text_input('What fruit would you like information about?')
#    #streamlit.write('The user entered ', fruit_choice)
#    if not fruit_choice:
#        streamlit.error("Please select a fruit to get information.")
#    else:
#        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#        #streamlit.text(fruityvice_response.json())
#        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#        streamlit.dataframe(fruityvice_normalized)
#
#except URLError as e:
#    streamlit. error()
#
#
#streamlit.stop()
### SNowflake connection
#
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
## my_data_row = my_cur.fetchone()
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)
#
#
## Allow the end user to add a fruit to the list
#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#streamlit.write('Thanks for adding ', add_my_fruit)
#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
#