from streamlit_option_menu import option_menu
import streamlit as st

def streamlit_menu():
    with st.sidebar:
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Project_Description", "Contact_Us", "Blog", "FAQ"],  # required
            icons=["house", "book", "envelope", "bootstrap", "question-circle"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )
    return selected







#
# import streamlit as st
# from streamlit_option_menu import option_menu
#
#
# def load_font_awesome():
#     # Load Font Awesome CSS
#     fa_css = """
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
#     integrity="sha512-Zs3spAF5yLv38PstCz6a02ylK1m0v2t4rjPBrReXlDbuZ+V3YAdW7mNezT+vQC0gzFpLEmYsIXL9GLZ9DRR42g=="
#     crossorigin="anonymous" referrerpolicy="no-referrer" />
#     """
#     st.markdown(fa_css, unsafe_allow_html=True)
#
# def streamlit_menu():
#     load_font_awesome()
#     with st.sidebar:
#         selected = option_menu(
#             menu_title=None,  # required
#             options=["Home", "Project Description", "Contact Us", "Blog", "FAQ"],  # required
#             icons=[
#                 '<i class="fas fa-home"></i>',
#                 '<i class="fas fa-book"></i>',
#                 '<i class="fas fa-envelope"></i>',
#                 '<i class="fas fa-blogger"></i>',
#                 '<i class="fas fa-question-circle"></i>'
#             ],  # optional
#             menu_icon="cast",  # optional
#             default_index=0,  # optional
#         )
#     return selected
