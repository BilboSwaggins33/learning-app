from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
from collections import Counter

import moviepy.editor as mp
import speech_recognition as sr
import os    
os.environ["FFMPEG_BINARY"] = "/usr/local/bin/ffmpeg"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input_form.html')

@app.route('/get_transcript', methods=['POST'])
def get_transcript():
    youtube_link = request.form['youtube_link']
    video_id = youtube_link.split('=')[1]
    print(type(video_id))
    try:
        transcript = YouTubeTranscriptApi.get_transcript(str(video_id))
        transcript_text = ' '.join([entry['text'] for entry in transcript])
    except Exception as e:
        transcript_text = "Error:" + str(e)
        return render_template('transcript.html', transcript=transcript_text)

    return render_template('transcript.html', transcript=transcript_text)

@app.route('/transcript_file', methods=['POST'])
def transcribe_file():
    file = request.files['file']
    video = mp.VideoFileClip(file)
    # Extract the audio from the video
    audio_file = video.audio
    audio_file.write_audiofile("geeksforgeeks.wav")
    # Initialize recognizer
    r = sr.Recognizer()
    # Load the audio file
    with sr.AudioFile("geeksforgeeks.wav") as source:
      data = r.record(source)
    # Convert speech to text
    text = r.recognize_google(data)
    # Print the text
    print("\nThe resultant text from video is: \n")
    print(text)
    return;

    

@app.route('/common_words', methods=['POST'])
def get_common_words():
    transcript_text = request.form['transcript']
    words = transcript_text.lower().split()
    common_words = Counter(words).most_common(20)  # Get the 10 most common words

    return render_template('common_words.html', common_words=common_words)

if __name__ == "__main__":
    app.run(debug=True)
