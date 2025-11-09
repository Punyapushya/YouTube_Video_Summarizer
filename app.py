# app.py
import streamlit as st
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi
from cohere_summary import generate_cohere_summary

# Load environment variables
load_dotenv()

prompt = (
    "You are a YouTube video summarizer. You will be taking the transcript text "
    "and summarizing the entire video and providing the important summary in points "
    "within 250 words. Please provide the summary of the text given here:  "
)

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript
    except Exception as e:
        raise e

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Detailed Notes"):
    try:
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            summary = generate_cohere_summary(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
    except Exception as e:
        st.error(f"Error: {str(e)}")
