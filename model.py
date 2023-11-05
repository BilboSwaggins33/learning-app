
import transformers
#from transformers import T5ForConditionalGeneration, T5Tokenizer
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
# model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
import requests


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def summarize_text(text):
    output = query({"inputs":text, "parameters": {"max_length":500000, "max_time": 15, "min_length": 10000} })
    return output[0]['summary_text']