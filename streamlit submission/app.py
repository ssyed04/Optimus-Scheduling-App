
##importing libraries

import streamlit as st
import requests
from streamlit_lottie import st_lottie
import random
import numpy as np
import time
from streamlit_calendar import calendar
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from Event import Event


st.set_page_config(page_title="Optimus", page_icon=":flexed_ups:", layout="wide")

motivationalQuotesFile = open("motivationalquotes.txt")
lines = motivationalQuotesFile.readlines()

eventList = [] ## list containing all event objects

def getMotivationalQuote():  ## function that generates motivational quotes and advice
    choice = random.choice(lines)
    return choice
    
def getInTouch():           ## form that users can enter with concerns 
    with st.container():
        st.write("---")
        st.header("Get in Touch!")

        contact_form = """
    <form action="https://formsubmit.co/sulaymansyed11@gmail.com" method="POST">
        <input type="text" name="name" placeholder = "Your name" required>
        <input type="email" name="email" placeholder = "your email" required>
        <textarea name = "message" placeholder = "your messsage here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()

def displayCalendar(events):              ##function that displays calendar
    st.title("""
              My Schedule
             """)
        
    data_matrix = [['TIME','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday'],
                ['00:00','','','','','','',''],
                ['01:00','','','','','','',''],
                ['02:00','','','','','','',''],
                ['03:00','','','','','','',''],
                ['04:00','','','','','','',''],
                ['05:00','','','','','','',''],
                ['06:00','','','','','','',''],
                ['07:00','','','','','','',''],
                ['08:00','','','','','','',''],
                ['09:00','','','','','','',''],
                ['10:00','','','','','','',''],
                ['11:00','','','','','','',''],
                ['12:00','','','','','','',''],
                ['13:00','','','','','','',''],
                ['14:00','','','','','','',''],
                ['15:00','','','','','','',''],
                ['16:00','','','','','','',''],
                ['17:00','','','','','','',''],
                ['18:00','','','','','','',''],
                ['19:00','','','','','','',''],
                ['20:00','','','','','','',''],
                ['21:00','','','','','','',''],
                ['22:00','','','','','','',''],
                ['23:00','','','','','','',''],
                ['24:00','','','','','','','']]

    myEvent = Event("13:00","20:00","23/09/2023", "Math Class")
    start = int(myEvent.startHr)
    end = int(myEvent.endHr)
    for i in range(end - start):
        data_matrix[start+1+i][4] = myEvent.location
    myEvent1 = Event("18:00","22:00","23/09/2023", "Soccer Practice")
    start1 = int(myEvent1.startHr)
    end1 = int(myEvent1.endHr)
    for i in range(end1 - start1):
        data_matrix[start1+1+i][3] = myEvent1.location
    myEvent2 = Event("12:00","18:00","23/09/2023", "Cornerstone Lab")
    start2 = int(myEvent2.startHr)
    end2 = int(myEvent2.endHr)
    for i in range(end2 - start2):
        data_matrix[start2+1+i][7] = myEvent2.location
    myEvent3 = Event("10:00","22:00","23/09/2023", "Volunteer Work")
    start3 = int(myEvent3.startHr)
    end3 = int(myEvent3.endHr)
    for i in range(end3 - start3):
        data_matrix[start3+1+i][1] = myEvent3.location
    myEvent4 = Event("10:00","17:00","23/09/2023", "Family Time")
    start4 = int(myEvent4.startHr)
    end4 = int(myEvent4.endHr)
    for i in range(end4 - start4):
        data_matrix[start+1+i][2] = myEvent4.location

    for i in range(7):          ##day
        for j in range(5):      ##time
            data_matrix[j+1][i+1] = "Sleep"

    for i in range(7):
        for j in range(2):
            data_matrix[j+24][i+1] = "Sleep"
    data_matrix[12][2] = "Crib"

    # for event in events:
    #     startTime = int(event.startHr)
    #     endTime = int(event.endHr)
    #     for i in range(endTime-startTime):
            
    fig = ff.create_table(data_matrix)
    st.plotly_chart(fig)

def schedule():         ##function for mySchedule page

    displayCalendar(eventList)
    if(st.button("Create New Event")):
        createUserEvent()

def landingPage():              ##function for landing page

    ##generating lottie gif
    local_css("style.css")
    lottie_coding = "https://lottie.host/dfbef0b1-57d5-4cba-b9df-39f81ae5163c/2THwKTEdoV.json"
    # ---------------------

    st.title("Hello! Welcome to Optimus.")
    st.subheader("The ultimate tool to balance your workload and organize your world! ")


    #---- waffle our blurb
    with st.container():
        st.write("----")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("__What We Do__")
            st.write("""Planning ahead and getting organized may be a stressful process. Optimus is dedicated to helping you set up a schedule that suits your needs and reminds you to take the occasional break. Tackling your to-do list and committing to a routine has never been easier.                     """)
        with right_column:
            st_lottie(lottie_coding, height = 300, key = "coding")

    if(st.button("Need Some Advice?")):
        sentence = getMotivationalQuote()
        st.write("## {}".format(sentence))
    getInTouch()


        ## -- our user event creation function 
def createUserEvent():
#    while st.button("Submit") == False:
#         date = st.date_input("Select a date", datetime.today())
#         categories = ["Meeting", "Workshop", "Presentation", "Other"]
#         category = st.selectbox("Select a category", categories)
#         starttime = st.text_input("Enter a start time in Military format")
#         endtime = st.text_input("Enter an end time in Military format")
#         repetitiveness_options = ["No Repetition", "Daily", "Every week", "Every two weeks", "Every three weeks", "Every month"]
#         repetitiveness = st.selectbox("Does this event repeat?", repetitiveness_options)

#         location = st.text_input("Location: ")

        with st.form(key = 'form1'):
            date = st.date_input("Select a date", datetime.today())
            categories = ["Meeting", "Workshop", "Presentation", "Other"]
            category = st.selectbox("Select a category", categories)
            starttime = st.text_input("Enter a start time in Military format")
            endtime = st.text_input("Enter an end time in Military format")
            repetitiveness_options = ["No Repetition", "Daily", "Every week", "Every two weeks", "Every three weeks", "Every month"]
            repetitiveness = st.selectbox("Does this event repeat?", repetitiveness_options)
            location = st.text_input("Location: ")
            if repetitiveness == "No Repetition":
                repetitiveness = 0
            elif repetitiveness == "Daily":
                repetitiveness = -1
            elif repetitiveness == "Every week":
                repetitiveness = 1
            elif repetitiveness == "Every two weeks":
                repetitiveness = 2
            elif repetitiveness == "Every three weeks":
                repetitiveness = 3
            elif repetitiveness == "Every month":
                repetitiveness = 4
            submit_button = st.form_submit_button(label = 'add event')
            

        if submit_button:
            container = st.empty()
            container.success("Event Created")
            time.sleep(2)
            container.empty()
            newEvent = Event(starttime, endtime, date, location, category, repetitiveness)
            eventList.append(newEvent)



        

    ##load lottie gif from internet
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

    ##load file from style.css
def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


    ## side bar to select page
page = st.sidebar.selectbox('Select Page',['Home','My Schedule']) 
if page == 'Home':
    landingPage()
    page = 1
if page == 'My Schedule':
    schedule()
    page = 2

