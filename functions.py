import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_data(user_input):
    """
    Transform user input into a pandas DataFrame

    PARAMETERS
    ----------
    user_input : dict
        dictionary containing the user input

    RETURNS
    -------
    df : pandas DataFrame
        DataFrame containing the user input
    """
    g_pattern = {
        "Subjective Significance of Work": 6,
        "Professional Ambition": 8,
        "Willingness to Overwork": 5,
        "Striving for Perfection": 6,
        "Ability to Distance Oneself": 6,
        "Tendency to Resign": 3,
        "Offensive Problem-Solving": 7,
        "Inner Calm": 7,
        "Sense of Achievement in Work": 7,
        "Life Satisfaction": 7,
        "Experience of Social Support": 6
    }
    s_data = {
        "Subjective Significance of Work": 2,
        "Professional Ambition": 2,
        "Willingness to Overwork": 2,
        "Striving for Perfection": 3,
        "Ability to Distance Oneself": 8,
        "Tendency to Resign": 4,
        "Offensive Problem-Solving": 4,
        "Inner Calm": 6,
        "Sense of Achievement in Work": 4,
        "Life Satisfaction": 6,
        "Experience of Social Support": 5
    }
    risk_a_data = {
        "Subjective Significance of Work": 8,
        "Professional Ambition": 6,
        "Willingness to Overwork": 8,
        "Striving for Perfection": 7,
        "Ability to Distance Oneself":2,
        "Tendency to Resign": 6,
        "Offensive Problem-Solving": 6,
        "Inner Calm": 3,
        "Sense of Achievement in Work": 6,
        "Life Satisfaction": 4,
        "Experience of Social Support": 4
    }
    risk_b_data = {
        "Subjective Significance of Work": 3,
        "Professional Ambition": 3,
        "Willingness to Overwork": 5,
        "Striving for Perfection": 4,
        "Ability to Distance Oneself": 4,
        "Tendency to Resign": 7,
        "Offensive Problem-Solving": 2,
        "Inner Calm": 3,
        "Sense of Achievement in Work": 2,
        "Life Satisfaction": 2,
        "Experience of Social Support": 4
    }

    data = pd.DataFrame([user_input, g_pattern, s_data, risk_a_data, risk_b_data]).T
    data.columns = ["User", "G-Pattern", "S-Pattern", "Risk A", "Risk B"]
    return data

def get_patterns(data):
    """
    Calculate the correlations between the user input and the other patterns

    PARAMETERS
    ----------
    data : pandas DataFrame
        DataFrame containing the user input

    RETURNS
    -------
    correlations : pandas DataFrame
        DataFrame containing the correlations between the user input and the other patterns
    """
    main_pattern = data.corrwith(data['User']).drop('User').idxmax()
    engagement = data.iloc[:4,:].corrwith(data.iloc[:4,:]['User']).drop('User').idxmax()
    tenacity = data.iloc[4:8,:].corrwith(data.iloc[4:8,:]['User']).drop('User').idxmax()
    emotions = data.iloc[8:,:].corrwith(data.iloc[8:,:]['User']).drop('User').idxmax()

    return main_pattern, engagement, tenacity, emotions

def plot_data(data, column_name='User', title=None):
    """
    Plot the user input and the other patterns

    PARAMETERS
    ----------
    data : pandas DataFrame
        DataFrame containing the user input

    RETURNS
    -------
    None
    """
    # plotting index of y axis and user values on x axis
    fig, ax= plt.subplots(1,1,figsize=(10, 6), facecolor='#d5e4ed')

    ax.plot(data[column_name], data.index, marker='o', label='User', color="#354e61")

    # Adjusting the coordinates of the fancy box

    # Adding text to the plot
    plt.text(-3.5, 2.5, 'Engagement', fontsize=12, color="#354e61", rotation=90)
    plt.text(-3.5, 6.25, 'Tenacity', fontsize=12, color="#354e61", rotation=90)
    plt.text(-3.5, 10, 'Emotions', fontsize=12, color="#354e61", rotation=90)

    plt.title(title, color="#354e61")
    plt.xticks(np.arange(0, 10, 1))
    plt.gca().set_facecolor('#d5e4ed')
    plt.gca().invert_yaxis()
    plt.grid()
    fig = plt.gcf()
    return fig

def sanitize_input(user_input):
    """
    Sanitize the user input

    PARAMETERS
    ----------
    user_input : dict
        dictionary containing the user input

    RETURNS
    -------
    user_input : dict
        dictionary containing the sanitized user input
    """
    for key, value in user_input.items():
        try:
            user_input[key] = int(value)
        except ValueError:
            user_input[key] = None
        
    return user_input