#Extractive Text Summarizer
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text = "Industry analysts agree on the importance of machine learning and its underlying algorithms. From Forrester, “Advancements in machine-learning algorithms bring precision and depth to marketing data analysis that helps marketers understand how marketing details—such as platform, creative, call to action, or messaging—impact marketing performance.1” While Gartner states that, “Machine learning is at the core of many successful AI applications, fueling its enormous traction in the market.Industry analysts agree on the importance of machine learning and its underlying algorithms. From Forrester, “Advancements in machine-learning algorithms bring precision and depth to marketing data analysis that helps marketers understand how marketing details—such as platform, creative, call to action, or messaging—impact marketing performance.1” While Gartner states that, “Machine learning is at the core of many successful AI applications, fueling its enormous traction in the market"

def summarizer(rawdoc):

    StopWord = list(STOP_WORDS)

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(rawdoc)


    token = [token.text for token in doc] #breaks doc in individual words
    # print(token)

    wordCount = {}
    for word in doc:
        if word.text.lower() not in StopWord and word.text.lower() not in punctuation:
            if word.text not in wordCount.keys():
                wordCount[word.text] = 1
            else:
                wordCount[word.text] += 1
    # print(wordCount)

    maxCount = max(wordCount.values())
    # print(maxCount)

    for word in wordCount.keys():
        wordCount[word]= wordCount[word]/maxCount # Normalized freq

    # print(wordCount)

    sentTokens= [sent for sent in doc.sents]
    # print(sentTokens)

    sentCount={}
    for sent in sentTokens:
        for word in sent:
            if word.text in wordCount.keys():
                if sent not in sentCount.keys():
                    sentCount[sent]= wordCount[word.text]
                else:
                    sentCount[sent]+= wordCount[word.text]
    # print(sentCount)

    length = int(len(sentTokens) * 0.4)
    print(length)


    Summary = nlargest(length,sentCount, key=sentCount.get)

    Summaryfinal = [word.text for word in Summary]
    Summary = " ".join(Summaryfinal)
    # print(Summary)
    # print(len(Summary.split(" ")))
    # print("_---------__--____")
    # print(text)
    # print(len(text.split(" ")))
    return doc , Summary, len(rawdoc.split(" ")), len(Summary.split(" "))

# print(summarizer(text))