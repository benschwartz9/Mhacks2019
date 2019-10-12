import nltk
from textblob import TextBlob


def simpleReturn():
    # insert user input to a text variable and replace sentence

    blob1 = TextBlob("Random jumble. with punctuation and spaces . hate words and love words.")

    my_list = []
    my_list2 = []

    # stores polarity and subjectivity of each sentence in a list

    for sentence in blob1.sentences:
        my_list.append(sentence.sentiment.polarity)
        my_list2.append(sentence.sentiment.subjectivity)


    x = my_list
    y = my_list2

    average_x = sum(x)/len(x)
    average_y = sum(y)/len(y)

    return average_x, average_y


# example blob for testing
# output = polarity = -0.8 and subjectivity = 0.9

#blob2 = TextBlob("I hate Donald Trump")

#print(format(blob2.sentiment))

