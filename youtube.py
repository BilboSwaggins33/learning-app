# from flask import Flask, render_template, request
# from youtube_transcript_api import YouTubeTranscriptApi
# from collections import Counter

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('input_form.html')

# @app.route('/get_transcript', methods=['POST'])
# def get_transcript():
#     youtube_link = request.form['youtube_link']
#     video_id = youtube_link.split('=')[1]

#     try:
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         transcript_text = ' '.join([entry['text'] for entry in transcript])
#     except Exception as e:
#         transcript_text = f"Error: {str(e)}"
#         return render_template('transcript.html', transcript=transcript_text)

#     return render_template('transcript.html', transcript=transcript_text)

# @app.route('/common_words', methods=['POST'])
# def get_common_words():
#     transcript_text = request.form['transcript']
#     words = transcript_text.lower().split()
#     common_words = Counter(words).most_common(20)  # Get the 10 most common words

#     return render_template('common_words.html', common_words=common_words)

# if __name__ == "__main__":
#     app.run(debug=True)
