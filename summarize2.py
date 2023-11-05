from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def choose_sentences_count(text_length):
    if text_length < 1000:
        return 5
    elif text_length < 2000:
        return 10
    elif text_length < 3000:
        return 15
    else:
        return 5


def return_summary(full_text):
    text = full_text

    text_length = len(text)
    sentences_count = choose_sentences_count(text_length)


    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count=sentences_count)    
    actual = ""
    for sentence in summary:
        actual += sentence
