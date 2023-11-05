from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
from collections import Counter
from summarize import get_summary
from model import summarize_text
import moviepy.editor as mp
import speech_recognition as sr
# Load the video
from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = './audiofiles'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    title = "hi"
    message  = "simple msg"
    return render_template('input_form.html', title=title, message=message)


@app.route('/get_transcript', methods=['POST'])
def get_transcript():
    youtube_link = request.form['youtube_link']
    percentage = int(request.form['percentage'])
    percentage = 3 - ((percentage/100) + 1);
    video_id = youtube_link.split('=')[1]


    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([entry['text'] for entry in transcript])
    except Exception as e:
        transcript_text = f"Error: {str(e)}"
        new_summary = get_summary(transcript_text)
        sum = summarize_text(transcript_text)
        return render_template('transcript.html', transcript=sum)

    sum = summarize_text(transcript_text)
    new_summary = get_summary(transcript_text, percentage)
    return render_template('transcript.html', transcript=sum, original_transcript=transcript_text)


@app.route('/common_words', methods=['POST'])
def get_common_words():
    transcript_text = request.form['transcript']
    words = transcript_text.lower().split()
    common_words = Counter(words).most_common(20)  # Get the 10 most common words


    return render_template('common_words.html', common_words=common_words)
if __name__ == '__main__':
    app.run()

@app.route('/transcript_file', methods=['POST'])
def transcript_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print(file)

    video = mp.VideoFileClip("audiofiles/" + filename)
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
    return render_template('transcript.html', transcript=text, original_transcript=text)

# @app.route("/hello")
# def hello():
#     return "you are now on hello"


# def h1():
#     return "<h1>Hello</h1>"

