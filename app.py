import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="About me", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("Style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
characterController = Image.open("characterController.jpg")
mqdefault = Image.open("mqdefault.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Faxxer :wave:")
    st.title("A python Programmer from India")
    st.write(
        "I am passionate about finding ways to use Python and automatig simple tasks that we find lazy ."
    )


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I use python to find various ways how we can automate simple tasks 
            that we find lazy in our daily life.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/channel/UC6zYw2Zrdpq6Jt2nf75o94A/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(characterController)
    with text_column:
        st.subheader("Make a smooth characterController in unity")
        st.write(
            """
            Learn how to create a smooth super responsive characterController in unity.

            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=4Jp5xSkEJ8s)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(mqdefault)
    with text_column:
        st.subheader("Make your player die and respawn in unity")
        st.write(
            """
            Make your player die and respawn in unity2d.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="divyanshsoni938.dec@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
