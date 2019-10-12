import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import numpy as np
import pandas as pd
import time

def analyze(url):
    ##url = "https://www.cnn.com/2019/10/11/politics/donald-trump-court-rulings-bad-day/index.html"

    # Request
    r1 = requests.get(str(url))

    # We'll save in coverpage the cover page content
    coverpage = r1.content

    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html.parser') #html5lib

    soup_article = BeautifulSoup(coverpage, 'html.parser') #html5lib

    x = soup_article.find_all('p')

    # same code but using the article contents instead of user
    list_paragraphs = []
    for p in np.arange(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = " ".join(list_paragraphs)

    blob1 = TextBlob(final_article)

    my_list = []
    my_list2 = []

    # stores polarity and subjectivity of each sentence in a list

    for sentence in blob1.sentences:
        my_list.append(sentence.sentiment.polarity)
        my_list2.append(sentence.sentiment.subjectivity)

    x2 = my_list
    y2 = my_list2

    average_x = sum(x2)/len(x2)
    average_y = sum(y2)/len(y2)

    return average_x, average_y
    # ^ values and averages to display