import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt

st.title('Contact Us')
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

st.subheader("Connect with Us on Social Media")
st.write("Follow us on social media for updates, news, and more!")
st.write("[Twitter](https://twitter.com/your_twitter_handle) :bird:")
st.write("[Facebook](https://facebook.com/your_facebook_page) :facebook:")
st.write("[LinkedIn](https://linkedin.com/in/your_linkedin_profile) :linkedin:")
