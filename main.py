import streamlit as st
import pandas

st.set_page_config(layout="wide")


st.title("The Best Company")
content = """
    Once upon a time, in a small town, there was a man named Dave who decided to adopt a parrot. Excited about his new pet, he went to the local pet store and found a parrot with vibrant feathers and a charming demeanor. The shopkeeper warned Dave that this particular parrot had been known to repeat everything it heard, which might be entertaining but could also be a bit much.
    """
st.info(content)


st.markdown("# Our Team")


col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")
#first name,last name,role,image


with col1:
    for index, row in df[:5].iterrows():
        st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.info(row["role"])
        st.image("images/" + row["image"])



with col2:
    for index, row in df[4:9].iterrows():
        st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.info(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[9:].iterrows():
        st.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.info(row["role"])
        st.image("images/" + row["image"])

