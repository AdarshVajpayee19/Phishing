# import streamlit as st
# import pandas as pd
#
# # from db_fxns import create_usertable, login_user, view_all_users, add_userdata
# # DB
# import sqlite3
#
# conn = sqlite3.connect('data.db')
# c = conn.cursor()
#
#
# # Functions
#
# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')
#
#
# def add_data(author, title, article, postdate):
#     c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',
#               (author, title, article, postdate))
#     conn.commit()
#
#
# def view_all_notes():
#     c.execute('SELECT * FROM blogtable')
#     data = c.fetchall()
#     return data
#
#
# def view_all_titles():
#     c.execute('SELECT DISTINCT title FROM blogtable')
#     data = c.fetchall()
#     return data
#
#
# def get_blog_by_title(title):
#     c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
#     data = c.fetchall()
#     return data
#
#
# def get_blog_by_author(author):
#     c.execute('SELECT * FROM blogtable WHERE author="{}"'.format(author))
#     data = c.fetchall()
#     return data
#
#
# def delete_data(title):
#     c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
#     conn.commit()
#
#
# def create_usertable():
#     c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
#
#
# def add_userdata(username, password):
#     c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
#     conn.commit()
#
#
# def login_user(username, password):
#     c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
#     data = c.fetchall()
#     return data
#
#
# def login_user_safe2(username, password):
#     c.execute("SELECT * FROM userstable WHERE username= '%s' AND password = '%s'"), (username, password);
#     data = c.fetchall()
#     return data
#
#
# # Works but not safe agains SQL injections
#
# def login_user_unsafe(username, password):
#     c.execute("SELECT * FROM userstable WHERE username='{}' AND password = '{}'".format(username, password))
#     data = c.fetchall()
#     return data
#
#
# def login_user_unsafe2(username, password):
#     c.execute(f"SELECT * FROM userstable WHERE username= '{username}' AND password= '{password}'")
#     data = c.fetchall()
#     return data
#
#
# def view_all_users():
#     c.execute('SELECT * FROM userstable')
#     data = c.fetchall()
#     return data
#
#
# st.title("Securing Login Apps Against SQL Injection")
#
#
# menu = ["Login","SignUp"]
# choice = st.sidebar.selectbox('Menu',menu)
#
#
# if choice == "Login":
# 	st.subheader("Login Into App")
# 	username = st.sidebar.text_input("Username")
# 	password = st.sidebar.text_input("Password",type='password')
# 	if st.sidebar.checkbox("Login"):
# 		create_usertable()
# 		result = login_user(username,password)
# 		# result = login_user_unsafe(username,password)
# 		# if password == "12345":
# 		if result:
# 			st.success("Logged In as {}".format(username))
#
# 			task = st.selectbox("Task",["Add Posts","Analytics","Manage"])
#
# 			if task == "Add Posts":
# 				st.subheader("Add Posts")
#
# 			elif task == "Analytics":
# 				st.subheader("Analytics")
#
# 			elif task == "Manage":
# 				st.subheader("Manage Blog")
# 				users_result = view_all_users()
# 				clean_db = pd.DataFrame(users_result,columns=["Username","Password"])
# 				st.dataframe(clean_db)
# 		else:
# 			st.warning("Incorrect Username/Password")
#
#
# elif choice =="SignUp":
# 	st.subheader("Create An Account")
# 	new_username = st.text_input("User name")
# 	new_password = st.text_input("Password",type='password')
# 	confirm_password = st.text_input('Confirm Password',type='password')
#
# 	if new_password == confirm_password:
# 		st.success("Valid Password Confirmed")
# 	else:
# 		st.warning("Password not the same")
#
# 	if st.button("Sign Up"):
# 		create_usertable()
# 		add_userdata(new_username,new_password)
# 		st.success("Successfully Created an Account")
#


import sqlite3

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
# import nlp as nlp
from wordcloud import WordCloud

# from wordcloud import WordCloud

# from wordcloud import WordCloud

matplotlib.use('Agg')
# Functions
# Avatar Image using a url
avatar1 = "https://www.w3schools.com/howto/img_avatar1.png"
avatar2 = "https://www.w3schools.com/howto/img_avatar2.png"


def readingTime(mytext):
    total_words = len([token for token in mytext.split(" ")])
    estimatedTime = total_words / 200.0
    return estimatedTime


import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")


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
	<h6>Author:{}</h6> 
	<h6>Post Date: {}</h6>
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
	<h6>Author:{}</h6> 		
	<h6>Post Date: {}</h6>		
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
    conn = sqlite3.connect('data.db')
    result = view_all_notes()
    conn.close()
    # st.subheader("Login Into App")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.checkbox("Login"):
        conn = sqlite3.connect('data.db')
        result = login_user(conn, username, password)
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
                st.subheader("Home")
                result = view_all_notes()
                for i in result:
                    # short_article = str(i[2])[0:int(len(i[2])/2)]
                    short_article = str(i[2])[0:50]
                    st.write(title_temp.format(i[1], i[0], short_article), unsafe_allow_html=True)

            # st.write(result)
            elif choice == "View Post":
                st.subheader("View Post")

                all_titles = [i[0] for i in view_all_titles()]
                postlist = st.sidebar.selectbox("Posts", all_titles)
                post_result = get_blog_by_title(postlist)
                for i in post_result:
                    st.text("Reading Time:{} minutes".format(readingTime(str(i[2]))))
                    st.markdown(head_message_temp.format(i[1], i[0], i[3]), unsafe_allow_html=True)
                    st.markdown(full_message_temp.format(i[2]), unsafe_allow_html=True)

                # if st.button("Analyze"):

                # 	docx = analyze_text(i[2])
                # 	html = displacy.render(docx,style="ent")
                # 	html = html.replace("\n\n","\n")
                # 	st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)




            elif choice == "Add Post":
                st.subheader("Add Your Article")
                create_table()
                blog_title = st.text_input('Enter Post Title')
                blog_author = st.text_input("Enter Author Name", max_chars=50)
                blog_article = st.text_area("Enter Your Message", height=200)
                blog_post_date = st.date_input("Post Date")
                if st.button("Add"):
                    add_data(blog_author, blog_title, blog_article, blog_post_date)
                    st.success("Post::'{}' Saved".format(blog_title))


            elif choice == "Search":
                st.subheader("Search Articles")
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
                st.subheader("Manage Blog")
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
                    st.subheader("Author Stats")
                    st.bar_chart(new_df['Author'].value_counts())  # Use st.bar_chart instead of plt.plot
                    st.subheader("Author Stats (Pie Chart)")
                    st.write(
                        new_df['Author'].value_counts().plot.pie(autopct="%1.1f%%"))  # Write the pie chart directly
                    st.pyplot()  # Display the pie chart

                if st.checkbox("WordCloud"):
                    st.subheader("Word Cloud")
                    text = ', '.join(clean_db['Article'])
                    wordcloud = WordCloud().generate(text)
                    plt.imshow(wordcloud, interpolation='bilinear')
                    plt.axis("off")
                    st.pyplot()

                if st.checkbox("BarH Plot"):
                    st.subheader("Length of Articles")
                    new_df = clean_db
                    new_df['Length'] = new_df['Article'].str.len()
                    barh_plot = new_df.plot.barh(x='Author', y='Length', figsize=(10, 10))
                    st.write(barh_plot)
                    st.pyplot()
            # st.dataframe(clean_db)
        else:
            st.warning("Incorrect Username/Password")

elif choice == "SignUp":
    st.subheader("Create An Account")
    new_username = st.text_input("User name")
    new_password = st.text_input("Password", type='password')
    confirm_password = st.text_input('Confirm Password', type='password')

    if new_password == confirm_password:
        st.success("Valid Password Confirmed")
    else:
        st.warning("Password not the same")

    if st.button("Sign Up"):
        add_userdata(new_username, new_password)
        st.success("Successfully Created an Account")
