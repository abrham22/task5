import streamlit as st
import pandas as pd
from add_data import db_execute_fetch

def main():
    st.title("Twitter Data Analytics Dashboard")

    st.sidebar.write("Navigation")
    app_mode = st.sidebar.selectbox("Choose Here", ("Home", "Sentiment Analysis","Topic Model"))
    if app_mode == 'Home':
        st.write('''
        ## The Data
        The data is collected from twitter. 
        Twitter is a social networking website that allows users to post real time messages, called tweets. 
        Tweets are short messages, restricted to 140 characters in length. 
        Due to the nature of this micro blogging service, people use acronyms, make spelling mistakes, use emojis,etc. The data format is a json file. This JSON file has a 50MB size. After we process it and change it to a data frame, it contains 6532 rows and 15 columns. 
        The key word that is used to collect the data is Covid19.
        ''')
        dataframe = db_execute_fetch("Select * from tweetinformation where (id < 6);", dbName = 'tweets')
        st.write('''
        ## The Head of the Data
        ''')
        st.table(dataframe)
        
    elif app_mode == 'Sentiment Analysis':
        st.write('''
        ## Sentiment Analysis
        In the sentiment analysis project, my SGDClassifier model achieved an accuracy of 99%.
        ''')
    elif app_mode == 'Topic Model':
        st.write('''
        ## Topic Modelling
        ### wordcloud
        ''')
        st.image('cloud.png')
    
if __name__ == "__main__":
    main()