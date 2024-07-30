import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable

def get_transcript(link):
    try:
        # Extracting video ID from the YouTube URL
        if "youtu.be" in link:
            vid_id = link.split("/")[-1].split("?")[0]
        else:
            vid_id = link.split("=")[-1].split("&")[0]
        
        # Getting transcript for the video
        data = yta.get_transcript(vid_id)
        
        # Processing transcript data
        final_data = ''
        for val in data:
            final_data += val['text'] + ' '
        
        return final_data.strip()
    except NoTranscriptFound:
        return "No transcript found for this video."
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except VideoUnavailable:
        return "The video is unavailable."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.title("YouTube Transcript Generator")

    # Input field for YouTube link
    link = st.text_input("Enter YouTube Video Link")

    if st.button("Get Transcript"):
        if link:
            transcript = get_transcript(link)
            st.subheader("Transcript:")
            st.text_area("Transcript Text", transcript, height=200)
        else:
            st.warning("Please enter a valid YouTube video link.")

if __name__ == "__main__":
    main()
