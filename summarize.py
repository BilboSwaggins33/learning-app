import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist



def get_summary(full_text):
    text = full_text
    words = word_tokenize(text)


    # removing stopwords
    stop_words = set(stopwords.words("english"))


    freqTable = dict()


    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1


    # print(freqTable)


    sentences = sent_tokenize(text)
    def get_sentence_value():
        sentence_value = dict()
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentence_value:
                        sentence_value[sentence] += freq
                    else:
                        sentence_value[sentence] = freq
        # print(sentence_value)
        return sentence_value


    sentence_value = get_sentence_value()
    # print(sentence_value)


    def get_sum_values():
        sum_values = 0
        for sentence in sentence_value:
            sum_values += sentence_value[sentence]


        average = int(sum_values / len(sentence_value))
        return average


    average = get_sum_values()
    # print(average)




    summary = ''
    for sentence in sentences:
        if (sentence in sentence_value) and (sentence_value[sentence] > (1.6 * average)):
            summary += " " + sentence
    return "This is the summary: " + summary



