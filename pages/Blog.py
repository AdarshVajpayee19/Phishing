import sqlite3

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import spacy
import streamlit as st
# import nlp as nlp
from wordcloud import WordCloud
from streamlit_option_menu import option_menu
# from wordcloud import WordCloud

# import spacy
# from wordcloud import WordCloud

import hashlib
import subprocess
# Download SpaCy model if not already downloaded
subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
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
# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


matplotlib.use('Agg')
# Functions
# Avatar Image using a url
avatar1 = "https://www.w3schools.com/howto/img_avatar1.png"
avatar2 = "https://www.w3schools.com/howto/img_avatar2.png"


def readingTime(mytext):
    total_words = len([token for token in mytext.split(" ")])
    estimatedTime = total_words / 200.0
    return estimatedTime



# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("venv/Lib/site-packages/en_core_web_sm")


def analyze_text(text):
    doc = nlp(text)
    return doc


# Now you can use analyze_text function to perform NLP tasks on your text data


# Layout Templates
title_temp = """
	<div style="background-color:#b5b5b5;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<h6>Author:{}</h6>
	<br/>
	<br/>	
	<p style="text-align:justify">{}</p>
	</div>
	"""
article_temp = """
	<div style="background-color:#b5b5b5;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<h6 style="color:white;text-align:center;">Author:{}</h6> 
	<h6 style="color:white;text-align:center;">Post Date: {}</h6>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>
	<p style="text-align:justify">{}</p>
	</div>
	"""
head_message_temp = """
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
	<h6 style="color:white;text-align:center;">Author:{}</h6> 		
	<h6 style="color:white;text-align:center;">Post Date: {}</h6>		
	</div>
	"""
full_message_temp = """
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<p style="text-align:justify;color:black;padding:10px">{}</p>
	</div>
	"""

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')
    conn.commit()
    conn.close()


def add_data(author, title, article, postdate):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',
              (author, title, article, postdate))
    conn.commit()
    conn.close()


def view_all_notes():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    conn.close()
    return data


def view_all_titles():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT title FROM blogtable')
    data = c.fetchall()
    conn.close()
    return data


def get_blog_by_title(title):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
    data = c.fetchall()
    conn.close()
    return data


def get_blog_by_author(author):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM blogtable WHERE author="{}"'.format(author))
    data = c.fetchall()
    conn.close()
    return data


def delete_data(title):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
    conn.commit()
    conn.close()


def create_usertable():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
    conn.commit()
    conn.close()


def add_userdata(username, password):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()
    conn.close()


def login_user(conn, username, password):
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def login_user_safe2(conn, username, password):
    c = conn.cursor()
    c.execute("SELECT * FROM userstable WHERE username= ? AND password = ?", (username, password))
    data = c.fetchall()
    return data


def login_user_unsafe(conn, username, password):
    c = conn.cursor()
    c.execute("SELECT * FROM userstable WHERE username='{}' AND password = '{}'".format(username, password))
    data = c.fetchall()
    return data


def login_user_unsafe2(conn, username, password):
    c = conn.cursor()
    c.execute(f"SELECT * FROM userstable WHERE username= '{username}' AND password= '{password}'")
    data = c.fetchall()
    return data


def view_all_users():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    conn.close()
    return data

def show():
    # UI
    # st.title("Securing Login Apps Against SQL Injection")
    # st.title("<span style='color:#4d6cc1'>Securing Login Apps Against SQL Injection</span>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#4d6cc1'>Phishing Blog</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    safe = """
    <span style="color:#4d6cc1"><b>Stay Safe Online:</b></span>  Watch out for fake emails and websites trying to trick you into sharing personal info. Check web addresses, be cautious with emails, and avoid clicking unknown links. Vigilance is key to staying safe from phishing scams.
    """
    description = """
    <span style="color:#4d6cc1"><b>Unveiling the Phishing Threat:</b></span> Dive into the world of phishing attacks and learn how cybercriminals manipulate unsuspecting users. Explore common tactics used to deceive individuals into revealing sensitive information. Discover essential tips to identify and avoid falling victim to phishing scams. Stay informed and arm yourself with the knowledge to protect your digital identity.
    """

    st.markdown(safe, unsafe_allow_html=True)
    st.markdown(description, unsafe_allow_html=True)

    menu = ["Login", "SignUp"]
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == "Login":
        create_table()  # Ensure table exists before attempting to fetch data
        st.markdown("<hr>",unsafe_allow_html=True)
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            conn = sqlite3.connect('data.db')
            hashed_password = hash_password(password)  # Hash the input password
            result = login_user(conn, username, hashed_password)  # Compare with hashed password in the database
            conn.close()
            if result:
                st.success("Logged In as {}".format(username))
                html_temp = """
                <div style="background-color:{};padding:10px;border-radius:10px">
                <h1 style="color:{};text-align:center;">Phishing Blog </h1>
                </div>
                """
                st.markdown(html_temp.format('#a3a7cf', 'white'), unsafe_allow_html=True)
                menu = ["Home", "View Post", "Add Post", "Search", "Manage Blog"]
                choice = st.sidebar.selectbox("Menu", menu)

                if choice == "Home":
                    st.markdown("<h3 style='color:#4d6cc1'>Blogs</h3>", unsafe_allow_html=True)

                    result = view_all_notes()
                    for i in result:
                        short_article = str(i[2])[0:50]
                        st.write(title_temp.format(i[1], i[0], short_article), unsafe_allow_html=True)

                elif choice == "View Post":
                    st.markdown("<h3 style='color:#4d6cc1'>View Post</h3>", unsafe_allow_html=True)

                    all_titles = [i[0] for i in view_all_titles()]
                    postlist = st.sidebar.selectbox("Posts", all_titles)
                    post_result = get_blog_by_title(postlist)
                    for i in post_result:
                        st.text("Reading Time:{} minutes".format(readingTime(str(i[2]))))
                        st.markdown(head_message_temp.format(i[1], i[0], i[3]), unsafe_allow_html=True)
                        st.markdown(full_message_temp.format(i[2]), unsafe_allow_html=True)

                elif choice == "Add Post":
                    st.markdown("<h3 style='color:#4d6cc1'>Add Your Article</h3>", unsafe_allow_html=True)
                    create_table()
                    blog_title = st.text_input('Enter Post Title')
                    blog_author = st.text_input("Enter Author Name", max_chars=50)
                    blog_article = st.text_area("Enter Your Message", height=200)
                    blog_post_date = st.date_input("Post Date")
                    if st.button("Add"):
                        add_data(blog_author, blog_title, blog_article, blog_post_date)
                        st.success("Post::'{}' Saved".format(blog_title))



                elif choice == "Search":
                    st.markdown("<h3 style='color:#4d6cc1'>Search Articles</h3>", unsafe_allow_html=True)
                    search_term = st.text_input("Enter Term")
                    search_choice = st.radio("Field to Search", ("title", "author"))
                    if st.button('Search'):
                        if search_choice == "title":
                            article_result = get_blog_by_title(search_term)
                        elif search_choice == "author":
                            article_result = get_blog_by_author(search_term)

                        # Preview Articles
                        for i in article_result:
                            st.text("Reading Time:{} minutes".format(readingTime(str(i[2]))))
                            # st.write(article_temp.format(i[1],i[0],i[3],i[2]),unsafe_allow_html=True)
                            st.write(head_message_temp.format(i[1], i[0], i[3]), unsafe_allow_html=True)
                            st.write(full_message_temp.format(i[2]), unsafe_allow_html=True)


                elif choice == "Manage Blog":
                    st.markdown("<h3 style='color:#4d6cc1'>Manage Blog</h3>", unsafe_allow_html=True)
                    result = view_all_notes()
                    clean_db = pd.DataFrame(result,
                                            columns=["Author", "Title", "Article", "Date"])  # Removed "Index" column
                    st.dataframe(clean_db)
                    unique_list = [i[0] for i in view_all_titles()]
                    delete_by_title = st.selectbox("Select Title", unique_list)
                    if st.button("Delete"):
                        delete_data(delete_by_title)
                        st.warning("Deleted: '{}'".format(delete_by_title))

                    if st.checkbox("Metrics"):
                        new_df = clean_db
                        new_df['Length'] = new_df['Article'].str.len()
                        st.dataframe(new_df)
                        # st.dataframe(new_df['Author'].value_counts())
                        st.markdown("<h3 style='color:#4d6cc1'>Author Stats</h3>", unsafe_allow_html=True)
                        st.bar_chart(new_df['Author'].value_counts())  # Use st.bar_chart instead of plt.plot

                        st.markdown("<h3 style='color:#4d6cc1'>Author Stats (Pie Chart)</h3>", unsafe_allow_html=True)
                        st.write(
                            new_df['Author'].value_counts().plot.pie(autopct="%1.1f%%"))  # Write the pie chart directly
                        st.pyplot()  # Display the pie chart

                    if st.checkbox("WordCloud"):
                        st.markdown("<h3 style='color:#4d6cc1'>Word Cloud</h3>", unsafe_allow_html=True)

                        text = ', '.join(clean_db['Article'])
                        wordcloud = WordCloud().generate(text)
                        plt.imshow(wordcloud, interpolation='bilinear')
                        plt.axis("off")
                        st.pyplot()

                    if st.checkbox("BarH Plot"):
                        st.markdown("<h3 style='color:#4d6cc1'>Length of Articles</h3>", unsafe_allow_html=True)

                        new_df = clean_db
                        new_df['Length'] = new_df['Article'].str.len()
                        barh_plot = new_df.plot.barh(x='Author', y='Length', figsize=(10, 10))
                        st.write(barh_plot)
                        st.pyplot()

            else:
                st.warning("Incorrect Username/Password")


    elif choice == "SignUp":
        st.markdown("<h3 style='color:#4d6cc1'>Create An Account</h3>", unsafe_allow_html=True)
        new_username = st.text_input("User name")
        new_password = st.text_input("Password", type='password', key='password_input')
        confirm_password = st.text_input('Confirm Password', type='password')

        if new_password != '' and confirm_password != '':
            if new_password == confirm_password:
                hashed_password = hash_password(new_password)  # Hash the password
                # add_userdata(new_username, hashed_password)  # Store hashed password in the database
                st.success("Valid Password Confirmed")
                if st.button("Sign Up"):
                    add_userdata(new_username, hashed_password)
                    # The sign-up button should perform no further action
                    st.success("Successfully Created an Account")
            else:
                st.warning("Password not the same")
        else:
            st.warning("Please fill in both password fields")

