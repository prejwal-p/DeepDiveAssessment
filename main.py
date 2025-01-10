import streamlit as st
import pandas as pd
from functions import *

main_pattern = None
engagement = None
tenacity = None
emotions = None
figure = plt.figure()
data = None
user_input = {
    "Subjective Significance of Work": None,
    "Professional Ambition": None,
    "Willingness to Overwork": None,
    "Striving for Perfection": None,
    "Ability to Distance Oneself": None,
    "Tendency to Resign": None,
    "Offensive Problem-Solving": None,
    "Inner Calm": None,
    "Sense of Achievement in Work": None,
    "Life Satisfaction": None,
    "Experience of Social Support": None
}

st.set_page_config(page_title="Burnout Risk and Workstyle Patterns", page_icon="🧠", layout="wide")

with st.sidebar:
    st.title("User Input")
    question_1 = st.text_input("Subjective Significance of Work", "")
    question_2 = st.text_input("Professional Ambition", "")
    question_3 = st.text_input("Willingness to Overwork", "")
    question_4 = st.text_input("Striving for Perfection", "")
    question_5 = st.text_input("Ability to Distance Oneself", "")
    question_6 = st.text_input("Tendency to Resign", "")
    question_7 = st.text_input("Offensive Problem-Solving", "")
    question_8 = st.text_input("Inner Calm", "")
    question_9 = st.text_input("Sense of Achievement in Work", "")
    question_10 = st.text_input("Life Satisfaction", "")
    question_11 = st.text_input("Experience of Social Support","")

    if st.button("Submit"):
        user_input["Subjective Significance of Work"] = question_1
        user_input["Professional Ambition"] = question_2
        user_input["Willingness to Overwork"] = question_3
        user_input["Striving for Perfection"] = question_4
        user_input["Ability to Distance Oneself"] = question_5
        user_input["Tendency to Resign"] = question_6
        user_input["Offensive Problem-Solving"] = question_7
        user_input["Inner Calm"] = question_8
        user_input["Sense of Achievement in Work"] = question_9
        user_input["Life Satisfaction"] = question_10
        user_input["Experience of Social Support"] = question_11

        user_input = sanitize_input(user_input)
        data = get_data(user_input)
        main_pattern, engagement, tenacity, emotions = get_patterns(data)
        figure = plot_data(data)


# Main Screen
st.title("Burnout Risk and Workstyle Patterns")
st.pyplot(figure)
st.divider()
st.write(f"Main Pattern: **{main_pattern}**")
st.divider()
st.write("Engagement Pattern: ", engagement)
st.write("Tenacity Pattern: ", tenacity)
st.write("Emotions Pattern: ", emotions)
st.divider()

st.header("Interpretation")

data = get_data(user_input)

st.divider()
columns = st.columns(4)
columns[0].subheader("G-Pattern")
columns[0].subheader("Health and Engaged")
columns[0].write("Clear, but not excessive, level of work commitment while maintaining the ability to distance oneself from work problems, aggressive coping behavior and resistance to stress, positive attitude to life Intervention not required from a health perspective!")
g_patt_fig = plot_data(data, column_name="G-Pattern")
columns[0].pyplot(g_patt_fig)

columns[1].subheader("S-Pattern")
columns[1].subheader("Protective")
columns[1].write("Low work commitment with strong distancing from work problems, psychological resilience to stress, (relative) satisfaction. Intervention is recommended less from a health perspective and more from a motivational aspect!")
s_patt_fig = plot_data(data, column_name="S-Pattern")
columns[1].pyplot(s_patt_fig)

columns[2].subheader("Risk A")
columns[2].subheader("Overcommitted")
columns[2].write("Excessive commitment and low detachment in relation to work problems (tendency to overtax yourself), reduced psychological resistance to stress, limited attitude to life. Intervention required from a health perspective!")
risk_a_fig = plot_data(data, column_name="Risk A")
columns[2].pyplot(risk_a_fig)

columns[3].subheader("Risk B")
columns[3].subheader("Withdrawn")
columns[3].write("Lower levels of work commitment (preferably in the importance of the work and in professional ambition), strong tendency to resignation and reduced psychological resistance to stress, significantly limited attitude to life. Intervention from a health perspective is required!")
risk_b_fig = plot_data(data, column_name="Risk B")
columns[3].pyplot(risk_b_fig)