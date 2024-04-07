import streamlit as st


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
    # Display the quiz
    st.markdown("<h1 style='color:#4d6cc1'>Phishing Quiz</h1>", unsafe_allow_html=True)

    # Quiz questions and answers
    questions = [
        "What is phishing?",
        "Which of the following is NOT a common phishing attack vector?",
        "What should you do if you receive a suspicious email?",
        "How can you recognize a phishing website?",
        "What can clicking a phishing link lead to?",
        "A legitimate email will always address you by:",
        "Phishing emails often contain a sense of:",
        "What is a common sign that a website may be a phishing site?",
        "When in doubt about the legitimacy of a website, it's best to:",
        "Which of the following is NOT a way to protect yourself from phishing attacks?"
    ]

    options = [
        ["A. A type of fishing", "B. A type of cyber attack", "C. A type of malware"],
        ["A. Email", "B. Phone call (Vishing)", "C. Radio broadcast"],
        ["A. Click on links or download attachments", "B. Ignore it entirely", "C. Report it as spam"],
        ["A. Check the URL for spelling errors", "B. Verify the sender's email address", "C. Both A and B"],
        ["A. Identity theft", "B. Malware infection", "C. Both A and C"],
        ["A. Your full name", "B. Your username or generic terms like 'customer'", "C. A nickname you use only with them"],
        ["A. Urgency or fear", "B. Gratitude or appreciation", "C. Curiosity or excitement"],
        ["A. Mismatched domain name and website content", "B. Typos or grammatical errors", "C. Both A and C"],
        ["A. Click the link and see where it goes", "B. Verify the website through a trusted source", "C. Ignore the website entirely"],
        ["A. Use strong and unique passwords", "B. Open suspicious attachments", "C. Share personal information only on secure websites"]
    ]

    correct_answers = ["B", "B", "C", "C", "C", "A", "A", "C", "B", "A"]

    # Display quiz questions and collect user answers
    score = 0
    # st.markdown("<h1 style='color:#4d6cc1'>Phishing Quiz</h1>", unsafe_allow_html=True)

    for i in range(len(questions)):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader(f"Question {i+1}: {questions[i]}")
        user_answer = st.radio("", options[i], key=f"answer_{i}")

        # Check and update score based on user answer
        if user_answer.split(".")[0].strip().upper() == correct_answers[i]:
            score += 1

    # Button to submit the quiz
    if st.button("Submit"):
        # Display the user's score
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h4 style='color:#4d6cc1'>Quiz Results</h4>", unsafe_allow_html=True)

        st.write(f"Your score: {score} out of {len(questions)}")

        # Display personalized feedback based on score
        if score >= 6:
            st.success("Congrats! You have a strong understanding of phishing attacks.")
            st.markdown("<hr>", unsafe_allow_html=True)
        else:
            st.error("While your score indicates room for improvement, don't worry! Here are some resources to help you learn more:")
            st.write("* [Phishing Information](https://www.cisa.gov/phishing)")
            st.write("* [Anti-Phishing Working Group](https://www.apwg.org/)")
            st.write("* [Stay Safe Online](https://staysafeonline.org/)")
            st.markdown("<hr>", unsafe_allow_html=True)







#
# import streamlit as st
#
# def phishing_quiz():
#     # Quiz questions and answers
#     questions = [
#         "What is phishing?",
#         "Which of the following is NOT a common phishing attack vector?",
#         "What should you do if you receive a suspicious email?",
#         "How can you recognize a phishing website?",
#         "What can clicking a phishing link lead to?",
#         "A legitimate email will always address you by:",
#         "Phishing emails often contain a sense of:",
#         "What is a common sign that a website may be a phishing site?",
#         "When in doubt about the legitimacy of a website, it's best to:",
#         "Which of the following is NOT a way to protect yourself from phishing attacks?"
#     ]
#
#     options = [
#         ["A. A type of fishing", "B. A type of cyber attack", "C. A type of malware"],
#         ["A. Email", "B. Phone call (Vishing)", "C. Radio broadcast"],
#         ["A. Click on links or download attachments", "B. Ignore it entirely", "C. Report it as spam"],
#         ["A. Check the URL for spelling errors", "B. Verify the sender's email address", "C. Both A and B"],
#         ["A. Identity theft", "B. Malware infection", "C. Both A and C"],
#         ["A. Your full name", "B. Your username or generic terms like 'customer'", "C. A nickname you use only with them"],
#         ["A. Urgency or fear", "B. Gratitude or appreciation", "C. Curiosity or excitement"],
#         ["A. Mismatched domain name and website content", "B. Typos or grammatical errors", "C. Both A and C"],
#         ["A. Click the link and see where it goes", "B. Verify the website through a trusted source", "C. Ignore the website entirely"],
#         ["A. Use strong and unique passwords", "B. Open suspicious attachments", "C. Share personal information only on secure websites"]
#     ]
#
#     correct_answers = ["B", "B", "C", "C", "C", "A", "A", "C", "B", "A"]
#
#     # Display quiz questions and collect user answers
#     score = 0
#     user_answers = []  # List to store user answers for all questions
#     for i in range(len(questions)):
#         st.subheader(f"Question {i+1}: {questions[i]}")
#         user_answer = st.radio("", options[i], key=f"answer_{i}")
#         user_answers.append(user_answer)
#
#     # Button to submit the quiz
#     if st.button("Submit"):
#         # Display the user's score
#         st.subheader("Quiz Result:")
#         if len(questions) > 0:
#             # Calculate score based on user answers and correct answers
#             for i in range(len(questions)):
#                 if user_answers[i] == correct_answers[i]:
#                     score += 1
#
#             st.write(f"Your score: {score} out of {len(questions)}")
#
#             # Calculate stars for score
#             stars = "⭐" * (score // (max(len(questions) // 5, 1)))
#
#             # Display stars representing the score
#             st.write({stars})
#
#             # Display correct answers and user answers for each question
#             for i in range(len(questions)):
#                 st.subheader(f"Question {i+1}: {questions[i]}")
#                 st.write("Correct Answer:")
#                 correct_answer_index = correct_answers.index(correct_answers[i])
#                 # If the index is valid, display the correct answer from the options list
#                 if 0 <= correct_answer_index < len(options[i]):
#                     st.success(options[i][correct_answer_index])
#                 else:
#                     st.write("An error occurred while displaying the correct answer.")
#                 st.write("Your Answer:")
#
#                 # Highlight the user's answer in green if correct, red if wrong
#                 if user_answers[i] == correct_answers[i]:
#                     st.success(user_answers[i])  # Display
# # Display the quiz
# st.title("Phishing Quiz")
# phishing_quiz()
