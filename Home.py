# import streamlit as st
# import machine_learning as ml
# import feature_extraction as fe
# from bs4 import BeautifulSoup
# import requests as re
# import matplotlib.pyplot as plt
#
# # col1, col2 = st.columns([1, 3])
#
# st.title('Phishing Website Detection using Machine Learning')
# st.write('This ML-based app is developed for educational purposes. Objective of the app is detecting phishing websites only using content data. Not URL!'
#          ' You can see the details of approach, data set, and feature set if you click on _"See The Details"_. ')
#
#
# with st.expander("PROJECT DETAILS"):
#     st.subheader('Approach')
#     st.write('We used _supervised learning_ to classify phishing and legitimate websites. '
#              'We benefit from content-based approach and focus on html of the websites. '
#              'Also, We used scikit-learn for the ML models.'
#              )
#     st.write('For this educational project, '
#              'We created my own data set and defined features, some from the literature and some based on manual analysis. '
#              'We used requests library to collect data, BeautifulSoup module to parse and extract features. ')
#     st.write('The source code and data sets are available in the below Github link:')
#     st.write('_https://github.com/AdarshVajpayee19/Phishing-Website-Detection-ML_')
#
#     st.subheader('Data set')
#     st.write('We used _"phishtank.org"_ & _"tranco-list.eu"_ as data sources.')
#     st.write('Totally 26584 websites ==> **_16060_ legitimate** websites | **_10524_ phishing** websites')
#
#     # ----- FOR THE PIE CHART ----- #
#     labels = 'phishing', 'legitimate'
#     phishing_rate = int(ml.phishing_df.shape[0] / (ml.phishing_df.shape[0] + ml.legitimate_df.shape[0]) * 100)
#     legitimate_rate = 100 - phishing_rate
#     sizes = [phishing_rate, legitimate_rate]
#     explode = (0.1, 0)
#     fig, ax = plt.subplots()
#     ax.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
#     ax.axis('equal')
#     st.pyplot(fig)
#     # ----- !!!!! ----- #
#
#     st.write('Features + URL + Label ==> Dataframe')
#     st.markdown('label is 1 for phishing, 0 for legitimate')
#     number = st.slider("Select row number to display", 0, 100)
#     st.dataframe(ml.legitimate_df.head(number))
#
#
#     @st.cache
#     def convert_df(df):
#         # IMPORTANT: Cache the conversion to prevent computation on every rerun
#         return df.to_csv().encode('utf-8')
#
#     csv = convert_df(ml.df)
#
#     st.download_button(
#         label="Download data as CSV",
#         data=csv,
#         file_name='phishing_legitimate_structured_data.csv',
#         mime='text/csv',
#     )
#
#     st.subheader('Features')
#     st.write('We used only content-based features. I didn\'t use url-based faetures like length of url etc.'
#              'Most of the features extracted using find_all() method of BeautifulSoup module after parsing html.')
#
#     st.subheader('Results')
#     st.write('We used 7 different ML classifiers of scikit-learn and tested them implementing k-fold cross validation.'
#              'Firstly obtained their confusion matrices, then calculated their accuracy, precision and recall scores.'
#              'Comparison table is below:')
#     st.table(ml.df_results)
#     st.write('NB --> Gaussian Naive Bayes')
#     st.write('SVM --> Support Vector Machine')
#     st.write('DT --> Decision Tree')
#     st.write('RF --> Random Forest')
#     st.write('AB --> AdaBoost')
#     st.write('NN --> Neural Network')
#     st.write('KN --> K-Neighbours')
#
# with st.expander('EXAMPLE PHISHING URLs:'):
#     st.write('_https://rtyu38.godaddysites.com/_')
#     st.write('_https://karafuru.invite-mint.com/_')
#     st.write('_https://defi-ned.top/h5/#/_')
#     st.caption('REMEMBER, PHISHING WEB PAGES HAVE SHORT LIFECYCLE! SO, THE EXAMPLES SHOULD BE UPDATED!')
#
# choice = st.selectbox("Please select your machine learning model",
#                  [
#                      'Gaussian Naive Bayes', 'Support Vector Machine', 'Decision Tree', 'Random Forest',
#                      'AdaBoost', 'Neural Network', 'K-Neighbours'
#                  ]
#                 )
#
# model = ml.nb_model
#
# if choice == 'Gaussian Naive Bayes':
#     model = ml.nb_model
#     st.write('GNB model is selected!')
# elif choice == 'Support Vector Machine':
#     model = ml.svm_model
#     st.write('SVM model is selected!')
# elif choice == 'Decision Tree':
#     model = ml.dt_model
#     st.write('DT model is selected!')
# elif choice == 'Random Forest':
#     model = ml.rf_model
#     st.write('RF model is selected!')
# elif choice == 'AdaBoost':
#     model = ml.ab_model
#     st.write('AB model is selected!')
# elif choice == 'Neural Network':
#     model = ml.nn_model
#     st.write('NN model is selected!')
# else:
#     model = ml.kn_model
#     st.write('KN model is selected!')
#
#
# url = st.text_input('Enter the URL')
# # check the url is valid or not
# if st.button('Check!'):
#     try:
#         response = re.get(url, verify=False, timeout=4)
#         if response.status_code != 200:
#             print(". HTTP connection was not successful for the URL: ", url)
#         else:
#             soup = BeautifulSoup(response.content, "html.parser")
#             vector = [fe.create_vector(soup)]  # it should be 2d array, so I added []
#             result = model.predict(vector)
#             if result[0] == 0:
#                 st.success("This web page seems a legitimate!")
#                 st.balloons()
#             else:
#                 st.warning("Attention! This web page is a potential PHISHING!")
#                 st.snow()
#
#     except re.exceptions.RequestException as e:
#         print("--> ", e)
#
#
#
#
#








import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Phishing Website Detection Using Machine Learning', page_icon='./static/favicon.png')
# Add the CSS rule using st.markdown
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
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
phishing_account_pic = current_dir / "static" / "Phishing-account.gif"


def applicationRun():

    # Add content for the Home page here
    # Set page title and description
    st.markdown("<h1 style='color:#c8a808'>Phishr</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#4d6cc1'>Phish the Phisher before they phish you!!!</h3>", unsafe_allow_html=True)

    # Add a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#4d6cc1'>Understanding Phishing Attack</4>", unsafe_allow_html=True)
    st.write('Phishing attacks are a common type of cyber attack where malicious actors attempt to deceive individuals or organizations into revealing '
             'sensitive information such as usernames, passwords, credit card numbers, or other personal or financial data. These attacks typically '
             'involve impersonating a trusted entity, such as a bank, a government agency, a company, or even a colleague or friend.')




    # st.image("static\Phishing-account.gif", use_column_width=True)
    # st.markdown(
    #     '<img src="phishing_account_pic">',
    #     unsafe_allow_html=True,
    # )
    #
    # # --- LOAD CSS, PDF & PROFIL PIC ---
    # with open(css_file) as f:
    #     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    # phishing_account_pic = Image.open(phishing_account_pic)


    # # --- HERO SECTION ---
    # col1, col2 = st.columns(2, gap="small")
    # with col1:
    #     st.image(phishing_account_pic)


    # Load the GIF
    phishing_acc = "static/Phishing-account.gif"

    # Display the GIF
    st.image(phishing_acc, caption='PHISHr', use_column_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    with st.expander('EXAMPLE PHISHING URLs:'):
        st.write('_https://rtyu38.godaddysites.com/_')
        st.write('_https://karafuru.invite-mint.com/_')
        st.write('_https://defi-ned.top/h5/#/_')
        st.caption('REMEMBER, PHISHING WEB PAGES HAVE SHORT LIFECYCLE! SO, THE EXAMPLES SHOULD BE UPDATED!')

    # Add a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)

    choice = st.selectbox("Please select your machine learning model",
                     [
                         'Gaussian Naive Bayes', 'Support Vector Machine', 'Decision Tree', 'Random Forest',
                         'AdaBoost', 'Neural Network', 'K-Neighbours'
                     ]
                    )

    model = ml.nb_model

    if choice == 'Gaussian Naive Bayes':
        model = ml.nb_model
        st.write('GNB model is selected!')
    elif choice == 'Support Vector Machine':
        model = ml.svm_model
        st.write('SVM model is selected!')
    elif choice == 'Decision Tree':
        model = ml.dt_model
        st.write('DT model is selected!')
    elif choice == 'Random Forest':
        model = ml.rf_model
        st.write('RF model is selected!')
    elif choice == 'AdaBoost':
        model = ml.ab_model
        st.write('AB model is selected!')
    elif choice == 'Neural Network':
        model = ml.nn_model
        st.write('NN model is selected!')
    else:
        model = ml.kn_model
        st.write('KN model is selected!')


    url = st.text_input('Enter the URL')
    # check the url is valid or not
    if st.button('Check!'):
        try:
            response = re.get(url, verify=False, timeout=4)
            if response.status_code != 200:
                print(". HTTP connection was not successful for the URL: ", url)
            else:
                soup = BeautifulSoup(response.content, "html.parser")
                vector = [fe.create_vector(soup)]  # it should be 2d array, so I added []
                result = model.predict(vector)
                if result[0] == 0:
                    st.success("This web page seems legitimate!")
                    # st.image("static\Safe.gif", use_column_width=True)
                    # st.markdown(
                    #     '<img src="./app/static/Safe.gif">',
                    #     unsafe_allow_html=True,
                    # )
                    # Load the GIF
                    Safe = "static/Safe.gif"

                    # Display the GIF
                    st.image(Safe, caption='Safe', use_column_width=True)
                    st.balloons()
                else:
                    st.warning("Attention! This web page is a potential phishing!")
                    # st.image("static\Warning.gif", use_column_width=True)
                    # st.markdown(
                    #     '<img src="./app/static/Warning.gif">',
                    #     unsafe_allow_html=True,
                    # )
                    # Load the GIF
                    warning = "static/Warning.gif"

                    # Display the GIF
                    st.image(warning, caption='Warning', use_column_width=True)
                    st.snow()

        except re.exceptions.RequestException as e:
            print("--> ", e)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#4d6cc1'>Mitigating Phishing Risks</h4>", unsafe_allow_html=True)

    st.write(
        'Phishing attacks pose significant risks to individuals, businesses, and organizations. They can lead to identity theft, financial loss, data breaches, '
        'and reputational damage. To protect against phishing attacks, it\'s essential to stay vigilant, be cautious of unsolicited emails or messages, '
        'verify the authenticity of websites and communications, and regularly update security measures such as antivirus software and firewalls. '
        'Additionally, education and awareness training for employees and users are crucial in preventing successful phishing attacks.')
    # Add a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)

    # # Add Navigation Bar Styling
    # st.markdown(
    #     """
    #     <style>
    #     .sidebar .sidebar-content {
    #         background-color: #f0f2f6;
    #     }
    #     .css-1aumxhk {
    #         color: #000000;
    #         background-color: #4CAF50;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

from menu import streamlit_menu
from pages import Blog, Project_Description, Contact_Us,FAQ

selected = streamlit_menu()

if selected == "Home":
    applicationRun()
if selected == "Project_Description":
    Project_Description.show()
elif selected == "Contact_Us":
    Contact_Us.show()
elif selected == "FAQ":
    FAQ.show()
elif selected == "Blog":
    Blog.show()

