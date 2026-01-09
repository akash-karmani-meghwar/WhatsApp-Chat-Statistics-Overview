# WhatsApp Chat Statistics Overview

A Python-based web application built with **Streamlit** to analyze and visualize WhatsApp chat data. This tool provides insights into message statistics, user activity, timelines, word clouds, and emoji usage from exported WhatsApp group or individual chats.

## 🌟 Features

- **Dashboard Overview**: View total messages, words, media shared, and links shared.
- **User Analysis**: Analyze the entire group or filter the analysis for a specific user.
- **Timeline Analysis**: 
  - Monthly timeline to see message trends over months.
  - Daily timeline for specific date activity.
- **Activity Maps**:
  - Identify the busiest days of the week.
  - Identify the busiest months.
  - Weekly Activity Heatmap (Day vs. Time of Day).
- **Most Busy Users**: A bar chart and percentage breakdown of the most active users in the group.
- **WordCloud**: A visual representation of the most frequent words used in the chat (excluding Hinglish stop words).
- **Most Common Words**: A horizontal bar chart showing the top 20 most common words.
- **Emoji Analysis**: A dataframe and pie chart displaying the frequency of emojis used.

## 📂 Project Structure

text
.
├── app.py                 # Main Streamlit application file
├── helper.py              # Helper functions for stats, analysis, and plots
├── preprocessor.py        # Script to parse raw WhatsApp text into DataFrame
├── requirements.txt       # List of Python dependencies
├── stop_hinglish.txt      # Text file containing common Hinglish stop words
├── verify_fix.py          # Utility script to verify date parsing logic
└── README.md              # This file


1. Export WhatsApp Chat:
    Open the WhatsApp chat (Group or Individual) you want to analyze.
    Go to Options (three dots)  More Export chat.
    Select Without Media.
   Save the `.txt` file to your computer.

2. Upload File:
    In the web app sidebar, click "Browse files" under "Choose a file".
    Select the exported `.txt` file.

3. Select User:
    Use the dropdown menu "Show analysis wrt" to select:
     Overal: Analyzes the entire group chat.
     Specific User: Analyzes only the messages sent by that specific person.

4. Analyze:
   Click the "Show Analysis" button.
   Browse through the different sections (Stats, Timelines, Activity Maps, WordCloud, etc.) generated below.

## 📊 Sample Data Analysis

This project includes a sample file `WhatsApp Chat with EE14-A official.txt`. You can test the application immediately using this file to see how the visualizations work.

## 🧠 Technical Details

Data Preprocessing: The `preprocessor.py` module uses Regular Expressions (Regex) to parse the standard WhatsApp export format (`MM/DD/YY, HH:MM - `). It extracts dates, users, messages, and splits them into a structured Pandas DataFrame.
Data Analysis: The `helper.py` module uses Pandas for aggregation and Matplotlib/Seaborn for plotting. It also u

## 📸 Preview Sections

1. Top Statistics: 4-column layout showing basic metrics.
2. Timelines: Line graphs showing chat activity over time.
3. Activity Heatmap: A grid showing when the group is most active (Hour vs Day).
4. WordCloud: A graphic image where the size of the word indicates its frequency.