import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    .css-wjbhl0.e1fqkh3o9 {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def show():

    st.markdown("<h1 style='color:#4d6cc1'>Contact Us</h1>", unsafe_allow_html=True)
    st.write("Have questions, feedback, or collaboration opportunities? "
             "Feel free to reach out to us using the contact form below "
             "or through our social media channels.")
    # Add content for the About Us page here
    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/adarshvajpayee19@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("styles/style.css")

    st.markdown("<h3 style='color:#4d6cc1'>Connect with Us on Social Media</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#4d6cc1'>Follow us on social media for updates, news, and more!</h4>", unsafe_allow_html=True)

    st.write("[Twitter](https://twitter.com/your_twitter_handle) :bird:")
    st.write("[Facebook](https://facebook.com/your_facebook_page) :facebook:")
    st.write("[LinkedIn](https://linkedin.com/in/your_linkedin_profile) :linkedin:")
