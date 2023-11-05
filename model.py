
# Import necessary modules
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
	output = query({"inputs":text, "parameters": {"max_length":500000, "max_time": 15,  "min_length": 10000} })
	return output[0]['summary_text']


# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
# A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
# Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
# In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
# Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
# 2010 marriage license application, according to court documents.
# Prosecutors said the marriages were part of an immigration scam.
# On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
# After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
# Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
# All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
# Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
# Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
# The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
# Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
# Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
# If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
# """
# print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))


# # Load the T5 model and tokenizer
# def summarize_text(text, maxLength):
#   model = T5ForConditionalGeneration.from_pretrained('t5-small')
#   tokenizer = T5Tokenizer.from_pretrained('t5-small')

#   # Define the input text and the summary length
#   max_length = 40

#   # Preprocess the text and encode it as input for the model
#   input_text = "summarize: " + text
#   input_ids = tokenizer.encode(input_text, return_tensors='pt')

#   # Generate a summary
#   summary = model.generate(input_ids, max_length=max_length)

#   # Decode the summary
#   summary_text = tokenizer.decode(summary[0], skip_special_tokens=True)
#   return summary_text