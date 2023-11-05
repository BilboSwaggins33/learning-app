from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
from collections import Counter
from exam import Exam
from model import summarize_text
import moviepy.editor as mp
import speech_recognition as sr
from werkzeug.utils import secure_filename
import os
from rake_nltk import Rake
# from summarize import get_summary
app = Flask(__name__)

UPLOAD_FOLDER = './audiofiles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
exams = []


@app.route("/")
def home():
    title = "hi"
    message  = "simple msg"
        
    return render_template('dashboard.html', title=title, message=message, exams=exams)

@app.route("/", methods=['POST'])
def addExam():
    title = "hi"
    message  = "simple msg"
    name = request.form['course_name']
    date = request.form['course_date']
    concepts = request.form['course_concepts'].split(" ")
    ex1 = Exam(name, date, concepts)

    exams.append(ex1)
    print(exams)
    return render_template('dashboard.html', title=title, message=message, exams=exams)



@app.route("/open_mindmap", methods=['POST'])
def mindmap():
    examId = request.form['exam']
    ex = [e for e in exams if e.id == int(examId)]
    return render_template('mindmap.html', exam=ex[0])

@app.route("/open_concept", methods=['POST'])
def concept():
    c = request.form['concept']
    return render_template('input_form.html', concept=c)

@app.route('/get_transcript', methods=['POST'])
def get_transcript():
    youtube_link = request.form['youtube_link']
    video_id = youtube_link.split('=')[1]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([entry['text'] for entry in transcript])
    except Exception as e:
        transcript_text = f"Error: {str(e)}"
        sum = summarize_text(transcript_text)
        return render_template('transcript.html', transcript=sum, original_transcript=transcript_text)

    sum = summarize_text(transcript_text)
    return render_template('transcript.html', transcript=sum, original_transcript=transcript_text)
    
@app.route('/key-concepts', methods=['POST'])
def get_common_words():
    r = Rake()
    transcript_text = request.form['transcript']
    r.extract_keywords_from_text(transcript_text)
    keywords = r.get_ranked_phrases()[0:10]# Get the 10 most common words

    return render_template('common_words.html', common_words=keywords)

@app.route("/transcript_file", methods=['POST'])
def transcribe_file():
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
    sum = summarize_text(text)

    return render_template('transcript.html', transcript=sum, original_transcript=text)




# if __name__ == '__main__':
#     app.run()

# @app.route("/hello")
# def hello():
#     return "you are now on hello"

# def h1():
#     return "<h1>Hello</h1>"